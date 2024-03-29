import re

def insert_certificates_path(file_path):
    # Step 1: Read the Markdown file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Step 2: Find and insert "Certificates/" right after the opening parenthesis
    # The regular expression pattern looks for the opening parenthesis and inserts "Certificates/" right after it
    modified_content = re.sub(r'\(', '(Certificates/', content)
    
    # Step 3: Write the modified content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(modified_content)

# Example usage
file_path = 'Readme.md'
insert_certificates_path(file_path)
