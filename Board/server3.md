# Project Code Snippets

## File: `server3.py`

```
from flask import Flask, send_from_directory, send_file, abort
import os

app = Flask(__name__)

# Define ALLOWED directories explicitly (security whitelist)
ALLOWED_DIRECTORIES = {
    'js', 'js/core', 'js/pages', 
    'styles', 'data', 'templates'
}

ALLOWED_EXTENSIONS = {
    '.js', '.css', '.html', '.json', '.txt'
}

def is_safe_path(path):
    """Security check to prevent directory traversal"""
    # Normalize path and check for directory traversal attempts
    normalized = os.path.normpath(path)
    if normalized.startswith('..') or normalized.startswith('/'):
        return False
    
    # Check if path is within allowed directories
    for allowed_dir in ALLOWED_DIRECTORIES:
        if normalized.startswith(allowed_dir):
            return True
    
    # Check root-level allowed files
    if '/' not in normalized and normalized in ['index.html', 'favicon.ico']:
        return True
        
    return False

def get_file_extension(filename):
    """Get file extension safely"""
    return os.path.splitext(filename)[1].lower()

@app.route('/')
def serve_index():
    """Serve only the main index page"""
    return send_file('templates/index.html')

@app.route('/<path:filename>')
def serve_file(filename):
    # Security checks
    if not is_safe_path(filename):
        abort(403, "Access denied")
    
    file_extension = get_file_extension(filename)
    if file_extension not in ALLOWED_EXTENSIONS:
        abort(403, f"File type {file_extension} not allowed")
    
    # Try to serve from exact path first
    if os.path.exists(filename) and os.path.isfile(filename):
        directory = os.path.dirname(filename) or '.'
        file_name = os.path.basename(filename)
        return send_from_directory(directory, file_name)
    
    # If not found, try common patterns (but only for allowed directories)
    for directory in ALLOWED_DIRECTORIES:
        full_path = os.path.join(directory, filename)
        if os.path.exists(full_path) and os.path.isfile(full_path):
            return send_from_directory(directory, filename)
    
    # File not found
    abort(404, f"File {filename} not found")

# Explicit routes for better security and clarity
@app.route('/js/<path:subpath>')
def serve_js(subpath):
    if not is_safe_path(f"js/{subpath}"):
        abort(403)
    return send_from_directory('js', subpath)

@app.route('/data/<path:filename>')
def serve_data(filename):
    if not is_safe_path(f"data/{filename}"):
        abort(403)
    return send_from_directory('data', filename)

@app.route('/styles/<path:filename>')
def serve_styles(filename):
    if not is_safe_path(f"styles/{filename}"):
        abort(403)
    return send_from_directory('styles', filename)

if __name__ == '__main__':
    print("🔒 SECURE Auto-serving IT Governance Dashboard")
    print("🌐 http://localhost:5000")
    print("📁 Whitelisted directories:", ALLOWED_DIRECTORIES)
    print("📄 Allowed file types:", ALLOWED_EXTENSIONS)
    
    # Security warnings
    if os.environ.get('FLASK_ENV') == 'production':
        print("⚠️  WARNING: Running in production mode")
        app.run(host='0.0.0.0', port=5000)
    else:
        app.run(debug=True, host='127.0.0.1', port=5000)
```

