"""Admin Panel Finder module for HackerBox."""
import sys
from pathlib import Path
from colorama import Fore
from typing import Optional

from config import DEFAULT_ADMIN_PANELS
from utils import make_request, show_progress_bar, show_notification, read_wordlist, logger

def AdminPanelFinder() -> None:
    """Find potential admin panels on a target website."""
    print(f"{Fore.RED}Warning: Enter your target address such as http://example.com{Fore.RESET}")
    url = input("Enter your target url: ").rstrip('/')

    wordlist_path = input("Enter location of admin panel text file (Press Enter to use default): ").strip()
    wordlist_file = Path(wordlist_path) if wordlist_path else DEFAULT_ADMIN_PANELS

    try:
        admin_paths = read_wordlist(wordlist_file)
        show_progress_bar("Initializing scan", 0.1)
        
        for path in admin_paths:
            target_url = f"{url}/{path.lstrip('/')}"
            try:
                response = make_request(target_url)
                if response.status_code == 200:
                    message = f"Admin panel found: {target_url}"
                    print(f"\n{'*' * 50}\n{message}\n{'*' * 50}")
                    show_notification(message)
                    break
                else:
                    print(f"{Fore.RED}Not found: {target_url}{Fore.RESET}")
            except Exception as e:
                logger.warning(f"Error checking {target_url}: {e}")
                continue

    except KeyboardInterrupt:
        logger.info("Scan interrupted by user")
        print(f"\n{Fore.RED}Scan interrupted by user{Fore.RESET}")
    except Exception as e:
        logger.error(f"Error during admin panel scan: {e}")
        print(f"\n{Fore.RED}Error: {e}{Fore.RESET}")
    
