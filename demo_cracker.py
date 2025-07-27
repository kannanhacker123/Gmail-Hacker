#!/usr/bin/env python3
import sys
import time

class Colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'

def print_banner():
    """Prints a clean and stylish banner."""
    print(f"{Colors.CYAN}=================================================={Colors.RESET}")
    print(f"{Colors.YELLOW}            Simulated Password Cracker         {Colors.RESET}")
    print(f"{Colors.CYAN}=================================================={Colors.RESET}")
    print(f"{Colors.BLUE}                 Author: ARAVIND K B               {Colors.RESET}")
    print(f"{Colors.BLUE}                     Version: 2.0 (Demo)           {Colors.RESET}")
    print()

def get_credentials():
    """Gets the target email, correct password, and password file path."""
    try:
        target_email = input(f"{Colors.YELLOW}[*] Enter a fake target email: {Colors.RESET}")
        correct_password = input(f"{Colors.YELLOW}[*] Enter the correct password for the simulation: {Colors.RESET}")
        password_file = input(f"{Colors.YELLOW}[*] Enter path to passwords file: {Colors.RESET}")
        return target_email, correct_password, password_file
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}[-] User interrupted. Exiting...{Colors.RESET}")
        sys.exit()

def display_progress(count, total, width=50):
    """Displays a simple progress bar."""
    percent = int((count / total) * 100)
    filled_length = int(width * count // total)
    bar = '█' * filled_length + '-' * (width - filled_length)
    sys.stdout.write(f'\r{Colors.GREEN}[*] Progress: |{bar}| {percent}% Complete({count}/{total}){Colors.RESET}')
    sys.stdout.flush()

def attempt_login_simulation(target_email, correct_password, password_list):
    """Simulates attempting to log in."""
    print(f"\n{Colors.YELLOW}[*] Starting simulation for {target_email}...{Colors.RESET}")
    
    for i, password in enumerate(password_list):
        password = password.strip()
        display_progress(i + 1, len(password_list))
        # time.sleep(0.1)  # Add a small delay to make the simulation visible

        if password == correct_password:
            print(f"\n{Colors.GREEN}[+] Password found: {password}{Colors.RESET}")
            return password
        else:
            # To avoid cluttering the output, we won't print every incorrect attempt
            pass

    print(f"\n{Colors.RED}[-] Password not found in the list.{Colors.RESET}")
    return None

def main():
    """Main function to run the script."""
    print_banner()
    target_email, correct_password, password_file = get_credentials()
    try:
        with open(password_file, 'r', encoding='utf-8', errors='ignore') as f:
            password_list = f.readlines()
        
        if not password_list:
            print(f"{Colors.RED}[-] Password file is empty.{Colors.RESET}")
            return

        attempt_login_simulation(target_email, correct_password, password_list)

    except FileNotFoundError:
        print(f"{Colors.RED}[-] Password file not found: {password_file}{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}[-] An error occurred: {e}{Colors.RESET}")

if __name__ == "__main__":
    main()
