import argparse
import time
import os
import random
import csv
from rich.table import Table
from rich.console import Console
from rich.theme import Theme
from rich.progress import Progress
from Nmap_scan import Nmap_main
from main import exploit_main
from art import art, ART_NAMES
from pyfiglet import Figlet
from rich.text import Text


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

# def print_ascii_art():
#     start_time=time.time()
#     ascii_art = """
                                                                                               
                                                                                               
#                AAA               PPPPPPPPPPPPPPPPP   TTTTTTTTTTTTTTTTTTTTTTT   SSSSSSSSSSSSSSS 
#               A:::A              P::::::::::::::::P  T:::::::::::::::::::::T SS:::::::::::::::S
#              A:::::A             P::::::PPPPPP:::::P T:::::::::::::::::::::TS:::::SSSSSS::::::S
#             A:::::::A            PP:::::P     P:::::PT:::::TT:::::::TT:::::TS:::::S     SSSSSSS
#            A:::::::::A             P::::P     P:::::PTTTTTT  T:::::T  TTTTTTS:::::S            
#           A:::::A:::::A            P::::P     P:::::P        T:::::T        S:::::S            
#          A:::::A A:::::A           P::::PPPPPP:::::P         T:::::T         S::::SSSS         
#         A:::::A   A:::::A          P:::::::::::::PP          T:::::T          SS::::::SSSSS    
#        A:::::A     A:::::A         P::::PPPPPPPPP            T:::::T            SSS::::::::SS  
#       A:::::AAAAAAAAA:::::A        P::::P                    T:::::T               SSSSSS::::S 
#      A:::::::::::::::::::::A       P::::P                    T:::::T                    S:::::S
#     A:::::AAAAAAAAAAAAA:::::A      P::::P                    T:::::T                    S:::::S
#    A:::::A             A:::::A   PP::::::PP                TT:::::::TT      SSSSSSS     S:::::S
#   A:::::A               A:::::A  P::::::::P                T:::::::::T      S::::::SSSSSS:::::S
#  A:::::A                 A:::::A P::::::::P                T:::::::::T      S:::::::::::::::SS 
# AAAAAAA                   AAAAAAAPPPPPPPPPP                TTTTTTTTTTT       SSSSSSSSSSSSSSS                                                                    
                               
# """
#     colors = ["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[34m", "\033[96m", "\033[33m"]  # ANSI escape codes for colors
#     text = " "
    
#     while True:
#         os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
        
#         # Generate a random color for each letter of "APTS"
#         colored_text = "".join(random.choice(colors) + letter for letter in text)
        
#         print(ascii_art)  # Print ASCII art
#         print(colored_text)  # Print colored "APTS" text
        
#         # Check if 5 seconds have passed
#         if time.time() - start_time >= 3:
#             break
        
#         time.sleep(0.1)  

valid_arts = ART_NAMES

def generate_random_art():
    # Select random text
    texts = ["Welcome", "Penetration Testing", "Cyber Resilience", "APTS", "Security", "Python CLI", "Metasploit"]
    random_text = random.choice(texts)

    # Select random ASCII art
    random_art = random.choice(valid_arts)

    return random_text, random_art

def display_art_with_animation():
    random_text, random_art = generate_random_art()
    
    # Generate ASCII text art
    figlet = Figlet(font='big')
    ascii_text = figlet.renderText(random_text)
    
    # Generate ASCII design art
    try:
        ascii_design = art(random_art)
    except:
        ascii_design = art("cat")  # Fallback to "cat" if there's an error

    # Combine both arts
    combined_art = f"{ascii_text}\n{ascii_design}"

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
    if args.Exploit:
        exploitable_csv_file , all_exploits_csv_file, complete_csv_file = Nmap_main(args.Exploit)
    else:
        exploitable_csv_file , all_exploits_csv_file, complete_csv_file = Nmap_main(args.ip_address)

def print_csv_as_table(file_name):
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
    if args.file_name in ['Exploitable.csv', 'Non_Exploitable.csv', 'complete_results.csv']:
        print_csv_as_table(args.file_name)
    else:
        console.print(f"[error]Invalid file name '{args.file_name}'.[/error]")
        console.print("[info]Please provide a valid file name: 'Exploitable.csv', 'Non_Exploitable.csv', or 'complete_results.csv'[/info]")

def open_all_command(args):
    print_csv_as_table('Exploitable.csv')
    console.rule()
    print_csv_as_table('Non_Exploitable.csv')
    console.rule()
    console.print("[bold magenta]Complete results[/bold magenta]")
    print_csv('complete_results.csv')

def print_csv(file_name):
    try:
        with open(file_name, 'r') as file:
            console.print(file.read())
    except FileNotFoundError:
        console.print(f"\n[bold red]File '{file_name}' not found.[/bold red]")
    except Exception as e:
        console.print(f"\n[bold red]Error printing CSV file: {e}[/bold red]")

def main():
    parser = argparse.ArgumentParser(description='Nmap CLI')
    parser.add_argument('--Sc', '--Scan', dest='ip_address', help='IP address to scan')
    parser.add_argument('--O', '--Open', dest='file_name', choices=['Exploitable.csv', 'Non_Exploitable.csv', 'complete_results.csv'], help='Open a report file [.csv]')
    parser.add_argument('--Oa', '--OpenAll', dest='OpenAll', action='store_true', help='Open all CSV files')
    parser.add_argument('--X', '--XBan', dest='No_Banner', action='store_true', help='Disable the banner')
    parser.add_argument('--Ex', '--Exploit', dest='Exploit', help='Exploit the vulnerabilities')
    parser.add_argument('--Vx', '--VerboseOff', dest='VerboseOff', action='store_true', help='Turn off verbose mode for exploitation')


    args = parser.parse_args()

    if not args.No_Banner:
        display_art_with_animation()
    
    if args.Exploit:
        scan_command(args)
        exploit_main(args.Exploit, verbose=not args.VerboseOff)
        console.rule()
    elif args.ip_address:
        scan_command(args)
        val = console.input("[bold magenta]Do you want to continue with the exploitation? [yes/no]: [/bold magenta]")
        if val.lower() == 'yes':
            exploit_main(args.Exploit, verbose=not args.VerboseOff)
            console.rule()
        console.rule()
    if args.file_name:
        open_command(args)
        console.rule()
    if args.OpenAll:
        open_all_command(args)
        console.rule()
    
    if not args.ip_address and not args.file_name and not args.OpenAll and not args.Exploit:
        console.print("[bold red]No arguments provided.[/bold red]")
        parser.print_help()

if __name__ == '__main__':
    main()
