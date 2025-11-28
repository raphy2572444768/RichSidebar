import os

def generate_markdown_from_project(directory):
    markdown_content = "# Project Code Snippets\n\n"

    # Traverse the directory
    for root, _, files in os.walk(directory):
        for file in files:
            # Get relative file path
            relative_path = os.path.relpath(os.path.join(root, file), start=directory)
            
            # Read file content with error handling for encoding
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
                    code = f.read()
            except Exception as e:
                code = f"Error reading file: {str(e)}"  # Handle file read errors gracefully

            # Append the markdown formatted content
            markdown_content += f"## File: `{relative_path}`\n\n"
            markdown_content += "```plaintext\n"  # Use 'plaintext' for general code formatting
            markdown_content += code
            markdown_content += "\n```\n\n"

    return markdown_content


if __name__ == '__main__':
    # Specify the directory to scan
    directory_path = 'Release/IT-DASHBOARD/v1.0.2'  # Change this to your project directory
    markdown_output = generate_markdown_from_project(directory_path)

    # Save the output to a markdown file
    with open('Release/IT-DASHBOARD/output_v1.0.2.md', 'w', encoding='utf-8') as output_file:
        output_file.write(markdown_output)

    print("Markdown file generated: output_v1.0.2.md")