import os

def generate_table(certificates):
    """Generates the Markdown table for the certificates."""
    table = "| Certificate | Provider |\n"
    table += "|---|---| \n"
    for cert in certificates:
        certificate_name = os.path.splitext(cert)[0].replace("%20", " ")
        table += f"| [{certificate_name}](./certificates/{cert}) |  |\n"
    return table

def main():
    """Updates the README.md file with the certificates table."""

    # Get all certificate images in the certificates folder
    certificates = [
        f
        for f in os.listdir("certificates")
        if os.path.isfile(os.path.join("certificates", f))
    ]

    # Generate the Markdown table
    table = generate_table(certificates)

    # Update README.md
    with open("README.md", "r") as readme_file:
        readme_content = readme_file.read()

    start_marker = "<!-- CERTIFICATES START -->"
    end_marker = "<!-- CERTIFICATES END -->"
    start_index = readme_content.find(start_marker) + len(start_marker)
    end_index = readme_content.find(end_marker)

    updated_readme = (
        readme_content[:start_index] + "\n" + table + "\n" + readme_content[end_index:]
    )

    with open("README.md", "w") as readme_file:
        readme_file.write(updated_readme)

if __name__ == "__main__":
    main()