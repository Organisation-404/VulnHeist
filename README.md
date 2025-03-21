# **VulnHeist** ⚔️ - Automated Penetration Testing Suite

## 🌐 Overview

**VulnHeist** is a powerful, automated tool 🔥 designed to simplify vulnerability scanning 🔍 and exploitation 💣. It combines the efficiency of **Nmap** 🌐 for scanning and the power of **Metasploit** 💻 for exploiting discovered vulnerabilities. Security professionals can enjoy a seamless, streamlined workflow 🛠️, with an easy-to-use interface designed for effective penetration testing.

## ✨ Key Features

- **Automated Nmap Scanning** 🌍: Detailed vulnerability scans powered by Nmap scripts.
- **Exploit Searching** 🔎: Finds applicable exploits using the **Metasploit** framework.
- **Automated Exploitation** 💥: Automatically exploits identified vulnerabilities with Metasploit.
- **Session Management** 💼: Opens, interacts with, and closes sessions seamlessly.
- **Detailed Logs & Reporting** 📊: Generates comprehensive reports in **Markdown** and **CSV** formats.
- **Interactive Console** 🎮: Rich-text console for real-time user interaction.

## 🔧 Requirements

- **Python 3.x** 🐍
- **Metasploit Framework** 💻
- **Nmap** 🌐
- Required Python packages:
  - `pymetasploit3`
  - `colorama`
  - `rich`
  - `libnmap`
  - `argparse`
  - `pyfiglet`
  - `matplotlib`

## 🚀 Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Organisation-404/VulnHeist
    cd VulnHeist
    ```

2. **Install required Python packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Ensure Metasploit & Nmap** are installed and configured on your system.

## ⚡ Usage

**VulnHeist** provides various command-line arguments for performing different tasks.

### Basic Commands

- **Scan an IP address**:
    ```bash
    VulnHeist -S <IP_ADDRESS>
    ```

- **Exploit an IP address**:
    ```bash
    VulnHeist -E <IP_ADDRESS>
    ```

- **Open a specific report**:
    ```bash
    VulnHeist -O <FILE_NAME>
    ```

- **Open all reports**:
    ```bash
    VulnHeist -Oa
    ```

### Command-Line Arguments

- **-S**: Scan the specified IP address.
- **-O**: Open report file (Exploitable.csv, All_exploits.csv, complete_results.csv).
- **-Oa**: Open all CSV reports.
- **-E**: Exploit vulnerabilities for the given IP.
- **-x**: Disable banner display.
- **-v**: Disable verbose mode during exploitation.

### Example Usage 🚨

1. **Scan & Exploit an IP**:
    ```bash
    VulnHeist -S 192.168.1.1
    VulnHeist -E 192.168.1.1
    ```

2. **Open Exploitable Report**:
    ```bash
    VulnHeist -O Exploitable.csv
    ```

3. **Open All Reports**:
    ```bash
    VulnHeist -Oa
    ```

### 🔄 Automated Workflow

1. **Scan an IP**:
    ```bash
    VulnHeist -S 192.168.1.1
    ```

2. **Review Results**:
    - Check reports like **Exploitable.csv**, **All_exploits.csv**, and **complete_results.csv**.

3. **Exploit Discovered Vulnerabilities**:
    ```bash
    VulnHeist -E 192.168.1.1
    ```

4. **Session Interaction**:
    VulnHeist handles session management for successful exploits.

## 💡 Contributing

We’re always excited to welcome new contributors to **VulnHeist**! 🌟 If you're passionate about cybersecurity and open-source development, feel free to submit issues, suggest features, or send in pull requests! Your unique skills and ideas can make a big difference.

## 📜 License

This project is licensed under the **BSD 3-Clause License (modified) with notification requirement**.

## ⚠️ Disclaimer

This tool is for **educational purposes only**. Unauthorized use is prohibited. Always ensure you have permission before scanning or testing any system.

## 👥 Authors

- [Sivasakthi N](https://github.com/sivasakthi037)
- [Vishaka Dheshini G](https://github.com/liyana9c) 
- [Shivanisree N](https://github.com/Shivanisree1603) 
- [Yogeshwaran R](https://github.com/yogeshwaranEvil) 

---

**Enjoy VulnHeist** and elevate your penetration testing game! 💥

