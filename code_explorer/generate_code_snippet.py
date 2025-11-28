import os
import re

def reconstruct_project_from_markdown_enhanced(markdown_file, output_directory, overwrite=False):
    """
    Enhanced version that reconstructs the complete project folder from markdown.
    
    Args:
        markdown_file (str): Path to the markdown file containing code snippets
        output_directory (str): Directory where the project structure will be recreated
        overwrite (bool): Whether to overwrite existing files (default: False)
    """
    
    # Create output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)
    
    # Check if output directory is empty (if not overwriting)
    if not overwrite and os.listdir(output_directory):
        response = input(f"Output directory '{output_directory}' is not empty. Overwrite? (y/n): ")
        if response.lower() != 'y':
            print("Operation cancelled.")
            return
    
    try:
        with open(markdown_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: Markdown file '{markdown_file}' not found.")
        return
    except Exception as e:
        print(f"Error reading markdown file: {str(e)}")
        return
    
    # Enhanced pattern to handle different markdown formats
    patterns = [
        r'## File: `([^`]+)`\s*```(?:plaintext|txt|code)?\n(.*?)\n```',
        r'## File: `([^`]+)`\s*```\n(.*?)\n```',
        r'### File: `([^`]+)`\s*```(?:plaintext|txt|code)?\n(.*?)\n```'
    ]
    
    files_processed = 0
    files_skipped = 0
    
    for pattern in patterns:
        matches = re.findall(pattern, content, re.DOTALL)
        if matches:
            break
    
    if not matches:
        print("No file sections found in the markdown file.")
        return
    
    for relative_path, code_content in matches:
        # Clean up the path and content
        relative_path = relative_path.strip()
        code_content = code_content.rstrip()
        
        # Skip empty files
        if not code_content.strip() and code_content.strip() != "Error reading file:":
            print(f"Skipped empty file: {relative_path}")
            files_skipped += 1
            continue
        
        # Construct full file path
        full_path = os.path.join(output_directory, relative_path)
        
        # Check if file already exists
        if os.path.exists(full_path) and not overwrite:
            print(f"Skipped (exists): {relative_path}")
            files_skipped += 1
            continue
        
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        
        try:
            # Write the file content
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(code_content)
            files_processed += 1
            print(f"Created: {relative_path}")
        except Exception as e:
            print(f"Error writing file '{relative_path}': {str(e)}")
    
    print(f"\nProject reconstruction completed!")
    print(f"Files processed: {files_processed}")
    print(f"Files skipped: {files_skipped}")
    print(f"Output directory: {output_directory}")

def main_enhanced():
    """
    Enhanced main function with command line argument support
    """
    import sys
    
    # Default values
    markdown_file = 'Release/IT-DASHBOARD/output_v1.0.2.md'
    output_directory = 'Release/IT-DASHBOARD/reconstructed_project_v1.0.2'
    overwrite = False
    
    # Parse command line arguments
    if len(sys.argv) > 1:
        markdown_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_directory = sys.argv[2]
    if len(sys.argv) > 3 and sys.argv[3].lower() in ['-o', '--overwrite', 'true', '1']:
        overwrite = True
    
    print(f"Input markdown file: {markdown_file}")
    print(f"Output directory: {output_directory}")
    print(f"Overwrite existing: {overwrite}")
    print("-" * 50)
    
    # Reconstruct the project
    reconstruct_project_from_markdown_enhanced(markdown_file, output_directory, overwrite)

if __name__ == '__main__':
    # Use the basic version
    # main()
    
    # Use the enhanced version
    main_enhanced()