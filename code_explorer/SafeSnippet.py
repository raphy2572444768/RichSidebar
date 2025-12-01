import os
import re
import customtkinter as ctk
import tkinter.filedialog as fd
from tkinter import BooleanVar, StringVar, Toplevel, Label, font as tkfont
import threading
import subprocess 
import platform 

try:
    # Attempt to import PyCryptodome components
    from Crypto.Cipher import AES
    from Crypto.Random import get_random_bytes
    from Crypto.Protocol.KDF import PBKDF2
    from Crypto.Hash import SHA256
    CRYPTO_AVAILABLE = True
except ImportError:
    CRYPTO_AVAILABLE = False


# --- Global Configuration and Patterns ---

# Configuration Constants for Cryptography
KEY_DERIVATION_ITERATIONS = 100000
KEY_LENGTH = 32
SALT_SIZE = 16

# Regex pattern for reconstructing project files from the Markdown archive format:
# It captures: ## File: `(relative_path)`\n\n```[lang]\n(code_content)\n```\n\n
# re.DOTALL is essential to allow the code content group (.*?) to match across newlines.
RECONSTRUCT_PATTERN = re.compile(
    r'## File: `([^`]+)`\s*\n+```[a-z]*\n(.*?)```\n\n', 
    re.DOTALL
)


# --- Utility Function to Open Folder (Cross-Platform) ---
def open_folder_in_explorer(path, log_callback):
    """
    Opens the given path (file or directory) in the native file explorer.
    Handles Windows, macOS, and Linux using platform-specific commands.
    """
    # 1. Ensure the path exists
    if not os.path.exists(path):
        log_callback(f"WARNING: Cannot open explorer. Path does not exist: {path}")
        return

    # 2. Determine the directory to open (if input is a file, open its parent directory)
    path_to_open = os.path.dirname(path) if os.path.isfile(path) else path
    
    system = platform.system()
    
    try:
        if system == "Windows":
            # Windows command to open the folder
            os.startfile(path_to_open) # os.startfile is generally preferred for simple opening on Windows
        elif system == "Darwin":
            # macOS command to open the folder
            subprocess.run(["open", path_to_open], check=True)
        elif system == "Linux":
            # Linux command (xdg-open is the standard command)
            subprocess.run(["xdg-open", path_to_open], check=True)
        else:
            log_callback(f"WARNING: Cannot automatically open folder on unknown OS: {system}")
            return
        
        log_callback(f"Opened output location in file explorer: {path_to_open}")

    except Exception as e:
        log_callback(f"ERROR: Failed to open folder explorer: {e}")


# --- Tooltip Class for customTkinter ---
class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tw = None
        self.id = None

        self.widget.bind("<Enter>", self.show)
        self.widget.bind("<Leave>", self.hide)

    def show(self, event=None):
        if self.id:
            self.widget.after_cancel(self.id)
        self.id = self.widget.after(500, self._show)

    def _show(self):
        if self.tw:
            return
        
        # Calculate position relative to the widget
        x_root = self.widget.winfo_rootx()
        y_root = self.widget.winfo_rooty()
        widget_height = self.widget.winfo_height()
        
        x_screen = x_root + 20
        y_screen = y_root + widget_height + 5 
        
        self.tw = Toplevel(self.widget)
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry(f"+{x_screen}+{y_screen}")
        
        label = Label(self.tw, 
                      text=self.text, 
                      justify='left',
                      background="#FFFFE0",
                      relief='solid', 
                      borderwidth=1,
                      font=("Arial", 9, "normal"))
        label.pack(ipadx=5, ipady=4)

    def hide(self, event=None):
        if self.id:
            self.widget.after_cancel(self.id)
        
        if self.tw:
            self.tw.destroy()
        self.tw = None

# --- Custom Dialog Class (RESIZED) ---
class CustomDialog(ctk.CTkToplevel):
    """A highly customizable modal dialog for confirmations and alerts."""
    def __init__(self, master, title, message, buttons, default_result=None):
        super().__init__(master)
        
        self.title(title)
        self.message = message
        self.buttons = buttons # List of (text, result_value, color) tuples
        self.result = default_result
        
        # Make the dialog modal
        self.transient(master)
        self.grab_set()
        
        # INCREASED SIZE FOR BETTER READABILITY AND BUTTON DISPLAY
        DIALOG_WIDTH = 500
        DIALOG_HEIGHT = 250
        
        # Center the dialog on the main window
        x = master.winfo_rootx() + (master.winfo_width() - DIALOG_WIDTH) // 2
        y = master.winfo_rooty() + (master.winfo_height() - DIALOG_HEIGHT) // 2
        self.geometry(f"{DIALOG_WIDTH}x{DIALOG_HEIGHT}+{x}+{y}")
        self.resizable(False, False)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Content Frame
        content_frame = ctk.CTkFrame(self)
        content_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        content_frame.grid_columnconfigure(0, weight=1)

        # Message Label - Increased wraplength to match new size
        msg_label = ctk.CTkLabel(content_frame, text=self.message, wraplength=DIALOG_WIDTH - 80, justify="center", font=ctk.CTkFont(size=14))
        msg_label.grid(row=0, column=0, padx=10, pady=(15, 20), sticky="ew")
        content_frame.grid_rowconfigure(0, weight=1) # Message takes available height

        # Button Frame
        button_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
        button_frame.grid(row=1, column=0, padx=10, pady=(0, 15), sticky="ew")
        
        # Configure columns for buttons - ensures even distribution
        for i in range(len(self.buttons)):
            button_frame.grid_columnconfigure(i, weight=1)
        
        # Create Buttons
        for i, (text, result_value, color) in enumerate(self.buttons):
            button = ctk.CTkButton(
                button_frame, 
                text=text, 
                fg_color=color,
                hover_color=color, # Using fg_color as hover_color for simplicity
                command=lambda res=result_value: self.on_button_click(res)
            )
            button.grid(row=0, column=i, padx=5, sticky="ew")

        self.protocol("WM_DELETE_WINDOW", self.on_close)
        # self.master.wait_window(self) # This is moved outside or called conditionally

    def on_button_click(self, result_value):
        self.result = result_value
        self.destroy()

    def on_close(self):
        # Handle close (e.g., set to default result or None)
        self.destroy()

# --- Cryptography and File Logic ---
def derive_key(password, salt):
    """Derives a secure AES key using PBKDF2."""
    if not CRYPTO_AVAILABLE:
        raise RuntimeError("PyCryptodome is not installed. Cannot perform key derivation.")
    password_bytes = password.encode('utf-8')
    key = PBKDF2(
        password_bytes,
        salt,
        dkLen=KEY_LENGTH,
        count=KEY_DERIVATION_ITERATIONS,
        hmac_hash_module=SHA256
    )
    return key

def encrypt_data(data, password):
    """Encrypts data using AES-256 GCM mode."""
    if not CRYPTO_AVAILABLE:
        raise RuntimeError("PyCryptodome is not installed. Cannot perform encryption.")
        
    salt = get_random_bytes(SALT_SIZE)
    key = derive_key(password, salt)
    
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(data.encode('utf-8'))
    
    # Format: salt | nonce | tag | ciphertext
    return salt + cipher.nonce + tag + ciphertext

def decrypt_data(encrypted_data, password):
    """Decrypts data using AES-256 GCM and verifies integrity."""
    if not CRYPTO_AVAILABLE:
        raise RuntimeError("PyCryptodome is not installed. Cannot perform decryption.")
        
    # Check minimum required length: Salt (16) + Nonce (16) + Tag (16) + at least 1 byte of data
    if len(encrypted_data) < SALT_SIZE + 16 + 16 + 1:
        raise ValueError("Encrypted data is too short or corrupted.")

    salt = encrypted_data[:SALT_SIZE]
    nonce = encrypted_data[SALT_SIZE:SALT_SIZE + 16]
    tag = encrypted_data[SALT_SIZE + 16:SALT_SIZE + 32]
    ciphertext = encrypted_data[SALT_SIZE + 32:]
    
    key = derive_key(password, salt)
    
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    
    # Decrypt and verify tag in one call
    plaintext_bytes = cipher.decrypt_and_verify(ciphertext, tag)
    
    return plaintext_bytes.decode('utf-8')

def extract_to_markdown(directory, log_callback):
    """Traverses the project directory and creates a single Markdown string."""
    markdown_content = f"# Project Archive: {os.path.basename(directory)}\n\n"
    log_callback(f"Traversing: {directory}...")

    # Pattern to exclude common non-code/system files and directories
    EXCLUDE_PATTERNS = ['.DS_Store', 'Thumbs.db', '__pycache__', '.git', '.svn', '.tmp', '~$']

    for root, dirnames, files in os.walk(directory):
        # Exclude common temporary/system directories from being traversed
        # Modifying dirnames in-place skips them in subsequent os.walk iterations
        dirnames[:] = [d for d in dirnames if not any(p in d for p in EXCLUDE_PATTERNS)]
        
        for file in files:
            file_path = os.path.join(root, file)
            
            # Check for exclusions in filenames
            if any(pattern in file for pattern in EXCLUDE_PATTERNS) or file.endswith('~'):
                continue
            
            relative_path = os.path.relpath(file_path, start=directory)
            
            # Skip binary files based on a simple check (can be improved with mimetypes)
            try:
                # Attempt to read as text
                with open(file_path, 'r', encoding='utf-8', errors='strict') as f:
                    code = f.read()
                
                # If reading succeeds, format and append
                markdown_content += f"## File: `{relative_path}`\n\n"
                file_extension = os.path.splitext(file)[1].lstrip('.')
                language_map = {'py': 'python', 'js': 'javascript', 'ts': 'typescript', 'html': 'html', 'css': 'css', 'md': 'markdown', 'json': 'json', 'yaml': 'yaml', 'txt': 'plaintext'}
                lang = language_map.get(file_extension, 'plaintext')
                
                markdown_content += f"```{lang}\n"
                markdown_content += code
                markdown_content += f"\n```\n\n"
                log_callback(f" -> Added: {relative_path}")
            
            except UnicodeDecodeError:
                # Skip known binary files (e.g., images, compiled executables)
                log_callback(f" -> SKIPPING (Binary/Undecodable): {relative_path}")
            except Exception as e:
                log_callback(f"WARNING: Failed to read {relative_path}. Error: {e}")
                
    return markdown_content

def _reconstruct_from_markdown_string(markdown_content, output_directory, log_callback):
    """
    (Core Logic) Parses markdown content and recreates the project folder structure.
    Uses the global RECONSTRUCT_PATTERN.
    """
    
    log_callback(f"\nStarting project reconstruction into: {output_directory}")
    
    matches = RECONSTRUCT_PATTERN.findall(markdown_content)
    files_processed = 0

    if not matches:
        log_callback("ERROR: No valid file blocks found in the markdown content.")
        return 0

    for relative_path, code_content in matches:
        try:
            full_path = os.path.join(output_directory, relative_path)
            
            # Ensure the subdirectory exists for the file
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            
            # The regex captures the final newline, so strip extra whitespace from the end of content
            final_content = code_content.rstrip() 
            
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(final_content)
                
            log_callback(f" -> Created file: {relative_path}")
            files_processed += 1
            
        except Exception as e:
            log_callback(f"WARNING: Failed to write file {relative_path}. Error: {e}")
            
    return files_processed

def reconstruct_project_from_markdown(input_path, output_path, log_callback):
    """
    (Wrapper) Reads a Markdown file and triggers the project reconstruction.
    output_path is the target directory for reconstruction.
    """
    log_callback(f"Reading plaintext Markdown from: {input_path}")
    
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
    except Exception as e:
        raise RuntimeError(f"Failed to read Markdown file: {e}")

    # The output_path variable holds the TARGET DIRECTORY in the GUI for this mode
    files_count = _reconstruct_from_markdown_string(markdown_content, output_path, log_callback)
    return files_count
    
# --- GUI Application Class (CustomTkinter) ---

class ProjectArchiverApp(ctk.CTk):
    
    def __init__(self):
        super().__init__()

        # Setup main window
        self.title("SafeSnippet - Secure Project Archiver")
        self.geometry("700x550")
        ctk.set_appearance_mode("System")  # Options: "Light", "Dark", "System"
        ctk.set_default_color_theme("blue")

        # Configure grid layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1) # Log area takes available space

        # Define the initial log message based on crypto availability
        self.initial_log_message = self._get_initial_log_message()

        # State Variables
        self.operation_mode = StringVar(value="extract")
        self.encrypt_var = BooleanVar(value=CRYPTO_AVAILABLE) # Default to True only if crypto is available
        self.input_path_var = StringVar(value="")
        self.output_path_var = StringVar(value="")
        self.password_var = StringVar(value="")
        
        # New variable for a third mode: Reconstruct
        self.operation_mode.trace_add("write", lambda name, index, mode: self.update_gui_mode())
        self.reconstruct_var = BooleanVar(value=False) # For the third mode option

        # Widgets
        self.setup_sidebar()
        self.setup_main_frame()
        self.setup_log_frame()
        
        # Initial GUI state based on mode
        self.update_gui_mode()
        
    def _get_initial_log_message(self):
        """Generates the correct starting message for the log."""
        if not CRYPTO_AVAILABLE:
            return (
                "WARNING: Cryptography (AES-256) is unavailable. "
                "Please install PyCryptodome (`pip install pycryptodome`) to enable encryption/decryption mode. "
                "Only plaintext extraction is currently possible."
            )
        else:
            return "Welcome! Select an operation mode and paths to begin."

    def setup_sidebar(self):
        """Creates the frame for mode selection and instructions."""
        sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=10)
        sidebar_frame.grid(row=0, column=0, rowspan=2, padx=20, pady=(20, 0), sticky="nsew")
        sidebar_frame.grid_columnconfigure(0, weight=1)
        
        # Title
        title_label = ctk.CTkLabel(sidebar_frame, text="CODEVAULT", font=ctk.CTkFont(size=16, weight="bold"))
        title_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        ToolTip(title_label, "Secure Project Archiver and Encryptor")
        
        # Mode selector (Radio Buttons)
        mode_header_label = ctk.CTkLabel(sidebar_frame, text="Operation Mode:", font=ctk.CTkFont(size=12))
        mode_header_label.grid(row=1, column=0, padx=20, pady=(10, 5), sticky="w")
        ToolTip(mode_header_label, "Choose whether to create an archive (Extract), decode an existing one (Decrypt), or turn Markdown back into a project (Reconstruct).")

        # Extract radio button
        extract_radio = ctk.CTkRadioButton(sidebar_frame, text="Extract & Encrypt", variable=self.operation_mode, value="extract", command=self.update_gui_mode)
        extract_radio.grid(row=2, column=0, padx=20, pady=5, sticky="w")
        ToolTip(extract_radio, "Extracts project files into a single Markdown, optionally encrypting it.")
        
        # Decrypt radio button
        decrypt_radio = ctk.CTkRadioButton(sidebar_frame, text="Decrypt Archive", variable=self.operation_mode, value="decrypt", command=self.update_gui_mode)
        decrypt_radio.grid(row=3, column=0, padx=20, pady=5, sticky="w")
        ToolTip(decrypt_radio, "Decrypts an encrypted binary (.bin) archive back into plaintext Markdown.")
        
        # Reconstruct radio button (New Mode)
        reconstruct_radio = ctk.CTkRadioButton(sidebar_frame, text="Reconstruct Project", variable=self.operation_mode, value="reconstruct", command=self.update_gui_mode)
        reconstruct_radio.grid(row=4, column=0, padx=20, pady=5, sticky="w")
        ToolTip(reconstruct_radio, "Takes a plaintext Markdown archive (.md) and rebuilds the project file structure.")
        
        # Separator
        ctk.CTkFrame(sidebar_frame, height=2, fg_color="#333", corner_radius=0).grid(row=5, column=0, padx=10, pady=15, sticky="ew")

        # Encryption Toggle (Switch) - Disabled if crypto is missing
        if CRYPTO_AVAILABLE:
            switch_text = "Enable Encryption (AES-256)"
        else:
            switch_text = "Encryption Unavailable (Install PyCryptodome)"

        self.encrypt_switch = ctk.CTkSwitch(
            sidebar_frame, 
            text=switch_text, 
            variable=self.encrypt_var, 
            onvalue=True, 
            offvalue=False,
            state="normal" if CRYPTO_AVAILABLE else "disabled", # Disable if crypto is missing
            command=self.update_gui_mode # Call update_gui_mode to reflect output path change
        )
        self.encrypt_switch.grid(row=6, column=0, padx=20, pady=(0, 20), sticky="w")
        ToolTip(self.encrypt_switch, "Toggles AES-256 encryption using GCM mode. Requires PyCryptodome.")


    def setup_main_frame(self):
        """Creates the frame for file paths and password input."""
        main_frame = ctk.CTkFrame(self, corner_radius=10)
        main_frame.grid(row=0, column=1, padx=20, pady=(20, 0), sticky="nsew")
        main_frame.grid_columnconfigure(1, weight=1)
        
        # --- Input Path Section ---
        self.input_label = ctk.CTkLabel(main_frame, text="Input Project Folder:", font=ctk.CTkFont(size=12, weight="bold"))
        self.input_label.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="w")
        ToolTip(self.input_label, "In 'Extract' mode: Select the root directory of your project.\nIn 'Decrypt' mode: Select the encrypted '.bin' archive file.\nIn 'Reconstruct' mode: Select the plaintext '.md' archive file.")
        
        self.input_entry = ctk.CTkEntry(main_frame, textvariable=self.input_path_var, placeholder_text="Path to Input (Folder or File)")
        self.input_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="ew")
        
        self.browse_input_button = ctk.CTkButton(main_frame, text="Browse Folder", command=self.browse_input)
        self.browse_input_button.grid(row=1, column=2, padx=(0, 10), pady=5, sticky="e")
        
        # --- Output Path Section ---
        self.output_label = ctk.CTkLabel(main_frame, text="Output File Path:", font=ctk.CTkFont(size=12, weight="bold"))
        self.output_label.grid(row=2, column=0, padx=10, pady=(10, 5), sticky="w")
        ToolTip(self.output_label, "In 'Extract' mode: Target file name (.md or .bin).\nIn 'Decrypt' mode: Target file name for decrypted Markdown (.md).\nIn 'Reconstruct' mode: Target directory for the reconstructed project files.")
        
        self.output_entry = ctk.CTkEntry(main_frame, textvariable=self.output_path_var, placeholder_text="Path to save the output (File or Folder)")
        self.output_entry.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

        self.browse_output_button = ctk.CTkButton(main_frame, text="Browse File", command=self.browse_output)
        self.browse_output_button.grid(row=3, column=2, padx=(0, 10), pady=5, sticky="e")

        # --- Password Section ---
        self.password_label = ctk.CTkLabel(main_frame, text="Encryption/Decryption Password (BYOK):", font=ctk.CTkFont(size=12, weight="bold"))
        self.password_label.grid(row=4, column=0, padx=10, pady=(10, 5), sticky="w")
        ToolTip(self.password_label, "This password is used to generate the AES key (via PBKDF2).\nRequired for encryption and decryption.")

        self.password_entry = ctk.CTkEntry(main_frame, textvariable=self.password_var, placeholder_text="Secure Password (required for Encrypt/Decrypt)", show="*")
        self.password_entry.grid(row=5, column=0, columnspan=3, padx=10, pady=(5, 10), sticky="ew")

        # --- Execute Button ---
        self.execute_button = ctk.CTkButton(main_frame, text="START OPERATION", 
                                             command=self.start_thread, 
                                             font=ctk.CTkFont(size=14, weight="bold"),
                                             height=40)
        self.execute_button.grid(row=6, column=0, columnspan=3, padx=10, pady=(10, 10), sticky="ew")

    def setup_log_frame(self):
        """Creates the frame for status and log output."""
        log_frame = ctk.CTkFrame(self, corner_radius=10)
        log_frame.grid(row=2, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")
        log_frame.grid_columnconfigure(0, weight=1)
        log_frame.grid_rowconfigure(1, weight=1)

        # Log Header Frame
        log_header_frame = ctk.CTkFrame(log_frame, fg_color="transparent")
        log_header_frame.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="ew")
        log_header_frame.grid_columnconfigure(0, weight=1)
        
        log_title_label = ctk.CTkLabel(log_header_frame, text="STATUS & LOG", font=ctk.CTkFont(size=14, weight="bold"))
        log_title_label.grid(row=0, column=0, sticky="w")
        ToolTip(log_title_label, "Displays status messages and detailed logs of file processing.")
        
        # Clear Log Button
        self.clear_log_button = ctk.CTkButton(log_header_frame, text="Clear Log", command=self.clear_log, width=80)
        self.clear_log_button.grid(row=0, column=1, sticky="e")
        
        self.log_textbox = ctk.CTkTextbox(log_frame, wrap="word")
        self.log_textbox.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="nsew")
            
        self.log_textbox.insert("end", self.initial_log_message)
        self.log_textbox.configure(state="disabled")

    def log_message(self, message):
        """Appends a message to the log area."""
        self.log_textbox.configure(state="normal")
        self.log_textbox.insert("end", "\n" + message)
        self.log_textbox.see("end")
        self.log_textbox.configure(state="disabled")

    def clear_log(self):
        """Clears the content of the log textbox and inserts the initial message."""
        self.log_textbox.configure(state="normal")
        self.log_textbox.delete("1.0", "end")
        
        # Insert the initial starting message
        self.log_textbox.insert("end", self._get_initial_log_message())
        
        self.log_textbox.configure(state="disabled")

    def browse_input(self):
        """Handles the 'Browse' action for the input path."""
        mode = self.operation_mode.get()
        if mode == "extract":
            # Browse for a Directory
            folder_path = fd.askdirectory(title="Select Project Folder to Archive")
            if folder_path:
                self.input_path_var.set(folder_path)
                # Suggest default output name based on folder
                base_name = os.path.basename(folder_path)
                ext = ".bin" if self.encrypt_var.get() and CRYPTO_AVAILABLE else ".md"
                self.output_path_var.set(f"{base_name}_archive{ext}")
                self.log_message(f"Selected project folder: {folder_path}")
        elif mode == "decrypt":
            if not CRYPTO_AVAILABLE:
                self.log_message("Error: Decryption mode requires PyCryptodome.")
                return
            # Browse for an Encrypted File
            file_path = fd.askopenfilename(title="Select Encrypted Archive File (.bin)", 
                                           filetypes=[("Binary Files", "*.bin"), ("All Files", "*.*")])
            if file_path:
                self.input_path_var.set(file_path)
                # Suggest default output name for decryption
                base_name = os.path.splitext(os.path.basename(file_path))[0]
                self.output_path_var.set(f"{base_name}_decrypted.md")
                self.log_message(f"Selected input file: {file_path}")
        elif mode == "reconstruct":
            # Browse for a Plaintext Markdown File
            file_path = fd.askopenfilename(title="Select Plaintext Markdown Archive (.md)", 
                                           filetypes=[("Markdown Files", "*.md"), ("Text Files", "*.txt"), ("All Files", "*.*")])
            if file_path:
                self.input_path_var.set(file_path)
                # Suggest default output directory
                base_name = os.path.splitext(os.path.basename(file_path))[0].replace('_archive', '').replace('_decrypted', '')
                self.output_path_var.set(f"{base_name}_reconstructed")
                self.log_message(f"Selected input file: {file_path}")


    def browse_output(self):
        """Handles the 'Browse' action for the output path."""
        mode = self.operation_mode.get()
        
        if mode == "reconstruct":
            # Output is a directory
            folder_path = fd.askdirectory(title="Select Output Directory for Project Reconstruction")
            if folder_path:
                self.output_path_var.set(folder_path)
                self.log_message(f"Selected output directory: {folder_path}")
            return # Exit function as directory is handled

        # For extract/decrypt, output is a file
        is_encrypt = self.encrypt_var.get() and CRYPTO_AVAILABLE
        
        if mode == "extract":
            if is_encrypt:
                file_types = [("Binary Archive", "*.bin")]
                default_ext = ".bin"
            else:
                file_types = [("Markdown File", "*.md")]
                default_ext = ".md"
            title_text = "Save Archive File"
        else: # decrypt mode
            file_types = [("Markdown File", "*.md")]
            default_ext = ".md"
            title_text = "Save Decrypted Plaintext File"

        # Ask where to save the file
        file_path = fd.asksaveasfilename(title=title_text, 
                                         defaultextension=default_ext,
                                         filetypes=file_types)
        if file_path:
            self.output_path_var.set(file_path)
            self.log_message(f"Selected output path: {file_path}")

    def update_gui_mode(self):
        """Updates UI elements based on the selected operation mode (Extract, Decrypt, or Reconstruct)."""
        mode = self.operation_mode.get()
        
        # 1. Update Labels and Browse Buttons
        if mode == "extract":
            self.input_label.configure(text="Input Project Folder:")
            self.output_label.configure(text="Output Archive File:")
            self.browse_input_button.configure(text="Browse Folder")
            self.browse_output_button.configure(text="Browse File")
            self.password_label.configure(text="Encryption Password (BYOK):")
            
            # Show encryption switch and adjust its state
            if CRYPTO_AVAILABLE:
                self.encrypt_switch.grid() 
            # self.encrypt_var.set(CRYPTO_AVAILABLE) # Keep the user's last selection
            self.password_entry.grid()
            
        elif mode == "decrypt":
            self.input_label.configure(text="Input Encrypted File:")
            self.output_label.configure(text="Output Markdown File:")
            self.browse_input_button.configure(text="Browse File")
            self.browse_output_button.configure(text="Browse File")
            self.password_label.configure(text="Decryption Password (BYOK):")
            
            # Hide encryption switch
            self.encrypt_switch.grid_remove() 
            self.encrypt_var.set(True) # Force crypto checks internally
            self.password_entry.grid()
            
        elif mode == "reconstruct":
            self.input_label.configure(text="Input Plaintext Markdown File:")
            self.output_label.configure(text="Output Project Directory:")
            self.browse_input_button.configure(text="Browse File")
            self.browse_output_button.configure(text="Browse Folder")
            
            # Hide password and encryption switch (not needed for plaintext reconstruction)
            self.encrypt_switch.grid_remove()
            self.password_entry.grid_remove()
            self.password_label.configure(text="Password (Not Required for Reconstruction):")
            
        # 2. Reset paths for clarity
        self.input_path_var.set("")
        self.output_path_var.set("")
        self.password_var.set("")
        self.log_message(f"\nSwitched to {mode.upper()} mode. Ready.")
        
    def start_thread(self):
        """Starts the main operation in a separate thread to keep the GUI responsive."""
        self.execute_button.configure(state="disabled", text="PROCESSING...")
        self.log_textbox.configure(state="normal")
        self.log_textbox.delete("1.0", "end")
        self.log_textbox.configure(state="disabled")
        self.log_message("Starting operation...")
        
        # Start the processing function in a new thread
        t = threading.Thread(target=self.run_operation)
        t.start()

    def _show_dialog_and_handle_result(self, title, message, buttons, action_handler, open_path=None, reconstruct_path=None):
        """
        Creates and waits for the CustomDialog, and then runs the action handler.
        This function is called via self.after() from the main thread.
        """
        dialog = CustomDialog(self, title, message, buttons, default_result="continue")
        
        # This line makes the dialog modal and pauses the main loop until the dialog closes
        self.wait_window(dialog)
        
        result = dialog.result
        
        # Action handler logic
        if result == "open_folder":
            open_folder_in_explorer(open_path, self.log_message)
        
        if result == "reconstruct_now":
            # Switch mode, set paths, and ask user to click START
            self.operation_mode.set("reconstruct")
            self.input_path_var.set(open_path) # Decrypted file becomes input
            
            # Suggest a reconstructed folder name
            base_name = os.path.splitext(os.path.basename(open_path))[0].replace('_archive', '').replace('_decrypted', '')
            suggested_dir = os.path.join(os.path.dirname(open_path), f"{base_name}_reconstructed")
            self.output_path_var.set(suggested_dir)

            self.log_message(f"\nMode switched to 'Reconstruct'. Input set to '{open_path}'.")
            self.log_message("Please verify the new output directory and click 'START OPERATION' to rebuild the project.")
            
        # Re-enable the button after the dialog is closed and actions are handled
        self.execute_button.configure(state="normal", text="START OPERATION")


    def run_operation(self):
        """Contains the main logic execution for the selected action."""
        mode = self.operation_mode.get()
        input_path = self.input_path_var.get()
        output_path = self.output_path_var.get()
        password = self.password_var.get()
        is_encrypt = self.encrypt_var.get() and CRYPTO_AVAILABLE # Only encrypt if toggle is ON AND crypto is available
        
        # --- Pre-Validation for Crypto Dependency ---
        if (mode == "decrypt" or is_encrypt) and not CRYPTO_AVAILABLE:
            self.log_message("Error: Cryptography is not available. Please install PyCryptodome.")
            self.execute_button.configure(state="normal", text="START OPERATION")
            return

        # --- Validation ---
        if not input_path or not output_path:
            self.log_message("Error: Both input and output paths must be selected.")
            self.execute_button.configure(state="normal", text="START OPERATION")
            return

        if (mode == "extract" and is_encrypt) or (mode == "decrypt"):
            if not password:
                self.log_message("Error: Password is required for encryption or decryption.")
                self.execute_button.configure(state="normal", text="START OPERATION")
                return

        # --- EXECUTION ---
        try:
            if mode == 'extract':
                if not os.path.isdir(input_path):
                    raise FileNotFoundError(f"Input directory not found: {input_path}")
                    
                # 1. Extract content
                plaintext_markdown = extract_to_markdown(input_path, self.log_message)
                
                if is_encrypt:
                    self.log_message("\nStarting AES-256 GCM encryption...")
                    encrypted_data = encrypt_data(plaintext_markdown, password)
                    
                    with open(output_path, 'wb') as f:
                        f.write(encrypted_data)
                    
                    final_msg = f"SUCCESS! Your project has been encrypted and archived to:\n\n{output_path}"
                    buttons = [
                        ("Open Output Folder", "open_folder", "green"),
                        ("Continue", "continue", "blue")
                    ]
                    
                else:
                    # Plaintext output
                    self.log_message("\nSaving plaintext archive (Encryption disabled)...")
                    with open(output_path, 'w', encoding='utf-8') as f:
                        f.write(plaintext_markdown)
                    
                    final_msg = f"SUCCESS! Your project archive has been saved as plaintext Markdown to:\n\n{output_path}"
                    buttons = [
                        ("Open Output Folder", "open_folder", "green"),
                        ("Continue", "continue", "blue")
                    ]
                
                self.log_message(f"Archive saved to: {output_path}")

                # FIX: Use lambda to correctly pass keyword arguments to self.after
                self.after(0, lambda: self._show_dialog_and_handle_result(
                           title="Extraction Complete", 
                           message=final_msg, 
                           buttons=buttons, 
                           action_handler=None, 
                           open_path=output_path))
                return


            elif mode == 'decrypt':
                if not os.path.exists(input_path):
                    raise FileNotFoundError(f"Input file not found: {input_path}")
                    
                self.log_message("\nStarting AES-256 GCM decryption...")

                with open(input_path, 'rb') as f:
                    encrypted_data = f.read()
                
                decrypted_markdown = decrypt_data(encrypted_data, password)
                
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(decrypted_markdown)
                    
                # Decryption successful, ask about reconstruction
                final_msg = f"SUCCESS! Decryption complete. Plaintext Markdown saved to:\n\n{output_path}\n\nDo you want to immediately reconstruct the project files?"
                buttons = [
                    ("Reconstruct Now", "reconstruct_now", "green"),
                    ("Open Output Folder", "open_folder", "blue"),
                    ("Later", "later", "gray")
                ]
                
                self.log_message(f"Decrypted content saved to: {output_path}")
                
                # FIX: Use lambda to correctly pass keyword arguments to self.after
                self.after(0, lambda: self._show_dialog_and_handle_result(
                           title="Decryption Complete", 
                           message=final_msg, 
                           buttons=buttons, 
                           action_handler=None, 
                           open_path=output_path))
                return
            
            elif mode == 'reconstruct':
                if not os.path.exists(input_path):
                    raise FileNotFoundError(f"Input file not found: {input_path}")
                    
                # Ensure output path exists or create it
                if not os.path.isdir(output_path):
                     os.makedirs(output_path, exist_ok=True)
                
                if not os.path.splitext(input_path)[1].lower() in ['.md', '.txt']:
                    self.log_message("Warning: Input file is not a .md or .txt file. Proceeding with reconstruction attempt...")

                self.log_message("\nStarting project reconstruction from Markdown...")
                
                # output_path is the directory in this mode
                files_count = reconstruct_project_from_markdown(input_path, output_path, self.log_message)
                
                final_msg = f"SUCCESS! Project reconstruction complete.\n\n{files_count} files rebuilt in:\n{output_path}"
                buttons = [
                    ("Open Reconstructed Project", "open_folder", "green"),
                    ("Continue", "continue", "blue")
                ]
                
                self.log_message(f"Reconstructed {files_count} files in: {output_path}")

                # FIX: Use lambda to correctly pass keyword arguments to self.after
                self.after(0, lambda: self._show_dialog_and_handle_result(
                           title="Reconstruction Complete", 
                           message=final_msg, 
                           buttons=buttons, 
                           action_handler=None, 
                           open_path=output_path))
                return

        except ValueError as ve:
            # Catches authentication failures (wrong password, corrupted data, or GCM tag failure)
            self.log_message(f"\nOPERATION FAILED: Verification failed (Wrong password or corrupted file).")
            self.log_message(f"Error Details: {ve}")
        except FileNotFoundError as fnfe:
            self.log_message(f"\nERROR: File or Folder not found. {fnfe}")
        except RuntimeError as re:
            # Catches the specific error for missing crypto during runtime check, or reconstruction read failures
            self.log_message(f"\nOPERATION FAILED: {re}")
        except Exception as e:
            self.log_message(f"\nOPERATION FAILED: An unexpected error occurred. Details: {e}")
        finally:
            # Only re-enable the button if an exception occurred before the dialog could be scheduled
            # Since successful paths return *before* finally, this only runs on error.
            # We use after(0) because this 'finally' block is running in the background thread.
            if self.execute_button.cget("state") == "disabled":
                self.after(0, lambda: self.execute_button.configure(state="normal", text="START OPERATION"))


if __name__ == '__main__':
    # Initial check and instruction display
    if not CRYPTO_AVAILABLE:
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!! WARNING: PyCryptodome is not installed.              !!")
        print("!! Encryption/Decryption features are disabled.         !!")
        print("!! Please run: pip install pycryptodome customtkinter   !!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
    else:
        print("PyCryptodome loaded successfully.")
        
    app = ProjectArchiverApp()
    app.mainloop()