const fs = require('fs');
const path = require('path');

const certificatesDir = path.join(__dirname, '..', '..', 'certificates');
const readmePath = path.join(__dirname, '..', '..', 'README.md');

// Read the certificates directory
const certificates = fs.readdirSync(certificatesDir);

// Generate the markdown for the certificates table
let certificatesMarkdown = '| Certificate | Provider |\n|---|---|\n';
for (const certificate of certificates) {
  const name = path.basename(certificate, path.extname(certificate)).replace(/%20/g, ' ');
  const provider = name.split(' ')[0]; // Extract the provider from the filename
  certificatesMarkdown += `| [${name}](${path.join('.', 'certificates', certificate)}) | ${provider} |\n`;
}

// Read the README
let readme = fs.readFileSync(readmePath, 'utf8');

// Replace the certificates section
readme = readme.replace(/<!-- CERTIFICATES START -->([\s\S]*?)<!-- CERTIFICATES END -->/, `<!-- CERTIFICATES START -->\n${certificatesMarkdown}<!-- CERTIFICATES END -->`);

// Write the README
fs.writeFileSync(readmePath, readme);