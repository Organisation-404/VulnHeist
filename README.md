# VulnHeist - Automated Penetration Testing Suite

## Overview

VulnHeist is a comprehensive tool designed to automate the process of vulnerability scanning and exploitation. It leverages Nmap for scanning and the Metasploit Framework for exploiting identified vulnerabilities. The suite aims to streamline the penetration testing workflow, providing an easy-to-use interface for security professionals.

## Features

- Automated Nmap Scanning: Performs detailed scans using Nmap scripts to identify vulnerabilities.
- Exploit Searching: Searches Metasploit for available exploits based on the scan results.
- Automated Exploitation: Attempts to exploit identified vulnerabilities with Metasploit.
- Session Management: Opens, interacts with, and closes sessions automatically.
- Logging and Reporting: Generates detailed logs and reports in Markdown and CSV formats.
- Interactive Console: Provides an interactive console with rich text output for user interactions.

## Requirements

- Python 3.x
- Metasploit Framework
- Nmap
- Required Python packages: 
  - pymetasploit3
  - colorama
  - rich
  - libnmap
  - argparse
  - pyfiglet
  - matplotlib

## Installation

1. Clone the repository:
    bash
    git clone https://github.com/Organisation-404/VulnHeist
    cd VulnHeist
    

2. Install the required Python packages:
    bash
    pip install -r requirements.txt
    

3. Ensure Metasploit and Nmap are installed and properly configured on your system.

## Usage

The VulnHeist can be executed with various command-line arguments to perform different tasks.

### Basic Commands

- Scan an IP address:
    bash
    VulnHeist -S <IP_ADDRESS>
    

- Exploit an IP address:
    bash
    VulnHeist -E <IP_ADDRESS>
    

- Open a specific report file:
    bash
    VulnHeist -O <FILE_NAME>
    

- Open all report files:
    bash
    VulnHeist -Oa
    

### Command-Line Arguments

- -S: IP address to scan.
- -O: Open a report file (Exploitable.csv, All_exploits.csv, complete_results.csv).
- -Oa: Open all CSV files.
- -x: Disable the banner.
- -E: Exploit the vulnerabilities of a given IP address.
- -v: Turn off verbose mode for exploitation.

### Example Usage

1. Scan and Exploit an IP Address:
    bash
    VulnHeist -S 192.168.1.1
    VulnHeist -E 192.168.1.1
    

2. Open the Exploitable Report:
    bash
    VulnHeist -O Exploitable.csv
    

3. Open All Reports:
    bash
    VulnHeist -Oa
    

### Automated Workflow

1. Scan an IP Address:
    bash
    VulnHeist -S 192.168.1.1
    

2. Check Results:
    - Review the generated reports (Exploitable.csv, All_exploits.csv, complete_results.csv).

3. Exploit Discovered Vulnerabilities:
    bash
    VulnHeist -E 192.168.1.1
    

4. Open Sessions and Interact:
    The tool will manage Metasploit sessions and provide interaction capabilities for successful exploits.

## Contributing

Contributions to VulnHeist are welcome! Feel free to submit issues or pull requests to improve the project.

## License

This project is licensed under the BSD 3-Clause License.

## Disclaimer

This tool is intended for educational purposes only. Unauthorized use of this tool is prohibited. Always obtain proper authorization before performing any penetration tests or scans on systems.

## Authors

- [Sivasakthi N](https://github.com/sivasakthi037)
- [Vishaka Dheshini G](https://github.com/liyana9c)
- [Shivanisree N](https://github.com/Shivanisree1603)
- [Yogeshwaran R](https://github.com/yogeshwaranEvil)
---

Enjoy using VulnHeist to enhance your security testing workflow!
