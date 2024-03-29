def add_sequential_numbers(file_path):
    # Step 1: Read the markdown file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Step 2: Initialize the counter for the numbering
    counter = 1

    # Step 3: Iterate through each line
    modified_lines = []
    for line in lines:
        # Step 4: Check if the line starts with ### (with a space after ###)
        if line.startswith('### '):
            # Step 5: Prepend the line with the current number and increment the number
            modified_line = f"{counter}. {line}"
            counter += 1
        else:
            modified_line = line

        # Add the modified line to the list
        modified_lines.append(modified_line)

    # Step 6: Write the modified lines back to the file
    with open(file_path, 'w') as file:
        file.writelines(modified_lines)
# Example usage
add_sequential_numbers('file.md')
