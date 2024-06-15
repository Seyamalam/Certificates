import re

with open('README.md', 'r') as file:
    content = file.read()

content = re.sub(r'%20', '_', content)

with open('README.md', 'w') as file:
    file.write(content)