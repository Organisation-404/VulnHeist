import argparse
import time
import os
import random
import csv
from rich.table import Table
from rich.console import Console
from rich.theme import Theme
from rich.progress import Progress
from Nmap_scan import Nmap_main, is_ip_scanned
from main import exploit_main
from art import art, ART_NAMES
from pyfiglet import Figlet
from rich.text import Text
import threading
from exploit_functions import manage_msfrpcd


# Define a custom theme with colors and styles
custom_theme = Theme({
    "info": "cyan",
    "warning": "yellow",
    "error": "bold red",
    "highlight": "bold magenta",
    "title": "bold blue",
    "table.header": "bold white on blue",
    "table.odd_row": "white",
    "table.even_row": "cyan",
})


console = Console(theme=custom_theme)



valid_arts = ART_NAMES

def generate_random_art():
    """
    Generate random text and ASCII art.

    Returns:
    - tuple: A tuple containing a random text and a random ASCII art
    """
 
    texts = ["Welcome", "Penetration Testing", "Cyber Resilience", "Security", "Automation", "Precision"]
    random_text = random.choice(texts)

    random_art = random.choice(valid_arts)

    return random_text, random_art

def display_art_with_animation():
    """
    Display random text and ASCII art with an animation effect, followed by a random promotional line.
    """
    random_text, random_art = generate_random_art()
    
   
    figlet = Figlet(font='big')
    ascii_text = figlet.renderText(random_text)
    
    
    try:
        ascii_design = art(random_art)
    except:
        ascii_design = art("cat")  

  
    combined_art = f"{ascii_text}"

    # Animate the display
    for line in combined_art.split('\n'):
        console.print(Text(line, style="bold green"))
        time.sleep(0.05)  # Sleep to create animation effect

    # Display random promotional line
    promo_lines = [
        "\nUnlock the future of security testing with APTS: Where automation meets precision.\n",
        "\nAccelerate penetration testing with APTS: Your all-in-one automation suite.\n",
        "\nExperience seamless testing with APTS: Your trusted partner in automated penetration testing.\n"
    ]
    console.print(Text(random.choice(promo_lines), style="bold green"))


def scan_command(args):
        """
    Execute the scan command based on the provided arguments.

    Args:
    - args: Command line arguments containing IP addresses to scan

    Returns:
    - tuple: Files containing scan results
    """
        if (args.exploit_ip_address):
            exploitable_csv_file , all_exploits_csv_file, complete_csv_file = Nmap_main(args.exploit_ip_address)
        else:
            exploitable_csv_file , all_exploits_csv_file, complete_csv_file = Nmap_main(args.scan_ip_address)


def print_csv_as_table(file_name):
    """
    Print the contents of a CSV file as a formatted table.

    Args:
    - file_name: The name of the CSV file to read and display
    """
    try:
        with open(file_name, 'r') as file:
            csv_reader = csv.DictReader(file)
            table = Table(title=f"[bold green]Results from {file_name}[/bold green]", show_header=True, header_style="table.header")

            # Add columns to the table
            table.add_column("IP Address", style="white")
            table.add_column("Port", style="white")
            table.add_column("Service", style="white")
            table.add_column("Version", style="white")
            table.add_column("Vulnerability IDs", style="white")

            # Add rows to the table
            for index, row in enumerate(csv_reader):
                style = "table.even_row" if index % 2 == 0 else "table.odd_row"  # Alternate row styles
                table.add_row(
                    row["IP Address"],
                    row["Port"],
                    row["Service"],
                    row["Version"],
                    row["Vulnerability IDs"],
                    style=style
                )

            console.print(table)
    except FileNotFoundError:
        console.print(f"[error]File '{file_name}' not found.[/error]")
    except Exception as e:
        console.print(f"[error]Error opening file: {e}[/error]")

def open_command(args):
    """
    Open and display the contents of a specified CSV file if it is valid.

    Args:
    - args: Command line arguments containing the file name to open
    """
    if args.file_name in ['Exploitable.csv', 'All_exploits.csv']:
        print_csv_as_table(args.file_name)
    elif args.file_name in [ 'complete_results.csv']:
        print_csv(args.file_name)
    else:
        console.print(f"[error]Invalid file name '{args.file_name}'.[/error]")
        console.print("[info]Please provide a valid file name: 'Exploitable.csv', 'All_exploits.csv', or 'complete_results.csv'[/info]")

def open_all_command(args):
    """
    Open and display the contents of all relevant CSV files sequentially with separators.

    Args:
    - args: Command line arguments (not used in this function)
    """
    print_csv_as_table('Exploitable.csv')
    console.rule()
    print_csv_as_table('All_exploits.csv')
    console.rule()
    console.print("[bold magenta]Complete results[/bold magenta]")
    print_csv('complete_results.csv')

def print_csv(file_name):
    """
    Print the entire contents of a CSV file.

    Args:
    - file_name: The name of the CSV file to read and print
    """
    try:
        with open(file_name, 'r') as file:
            console.print(file.read())
    except FileNotFoundError:
        console.print(f"\n[bold red]File '{file_name}' not found.[/bold red]")
    except Exception as e:
        console.print(f"\n[bold red]Error printing CSV file: {e}[/bold red]")

def main():
    parser = argparse.ArgumentParser(description='Automated Penetration Testing Suite (APTS)')

    parser.add_argument('-S', dest='scan_ip_address', help='IP address to scan')
    parser.add_argument('-O',dest='file_name', choices=['Exploitable.csv', 'All_exploits.csv', 'complete_results.csv'], help='Open a report file [.csv]')
    parser.add_argument('-Oa', dest='OpenAll', action='store_true', help='Open all CSV files')
    parser.add_argument('-x', dest='No_Banner', action='store_true', help='Disable the banner')
    parser.add_argument('-E',  dest='exploit_ip_address', help='Exploit the vulnerabilities')
    parser.add_argument('-v',  dest='VerboseOff', action='store_true', help='Turn off verbose mode for exploitation')

    args = parser.parse_args()
    scanned_ips_file = 'scanned_ips.csv'

    
    
    if not args.No_Banner:
        display_art_with_animation()

    msfrpcd_thread = threading.Thread(target=manage_msfrpcd)
    msfrpcd_thread.start()
 
    if args.exploit_ip_address:
        
        
        if is_ip_scanned(args.exploit_ip_address, scanned_ips_file):
            print(f"The IP address {args.exploit_ip_address} has already been scanned.")
        else:
            scan_command(args)

        exploit_main(args.exploit_ip_address, verbose=not args.VerboseOff)
        
    elif args.scan_ip_address:
        scan_command(args)
        val = console.input("[bold magenta]Do you want to continue with the exploitation? (y/n): [/bold magenta]")
        if val.lower() == 'y':
            exploit_main(args.scan_ip_address, verbose=not args.VerboseOff)
            
    if args.file_name:
        open_command(args)
        
    if args.OpenAll:
        open_all_command(args)
        
    
    if not args.exploit_ip_address and not args.file_name and not args.OpenAll and not args.scan_ip_address:
        console.print("[bold red]No arguments provided.[/bold red]")
        parser.print_help()
if __name__ == '__main__':
    main()
