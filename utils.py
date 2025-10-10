"""Utility functions for HackerBox."""

import logging
import requests
import time
from pathlib import Path
from typing import Optional
from prompt_toolkit.shortcuts import ProgressBar
from prompt_toolkit.styles import Style
from prompt_toolkit.shortcuts.progress_bar import formatters
from plyer import notification

from config import (
    NOTIFICATION_ICON,
    NOTIFICATION_TIMEOUT,
    PROGRESS_BAR_STYLE,
    REQUEST_TIMEOUT,
    LOG_FILE,
    LOG_FORMAT
)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    format=LOG_FORMAT,
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def show_progress_bar(text: str, duration: float) -> None:
    """Display a customized progress bar.
    
    Args:
        text: Text to display alongside the progress bar
        duration: Time in seconds for each progress increment
    """
    try:
        style = Style.from_dict(PROGRESS_BAR_STYLE)
        custom_formatters = [
            formatters.Label(),
            formatters.Text(': [', style='class:percentage'),
            formatters.Percentage(),
            formatters.Text(']', style='class:percentage'),
            formatters.Text(' '),
            formatters.Bar(sym_a='#', sym_b='#', sym_c='.'),
            formatters.Text('  '),
        ]

        with ProgressBar(style=style, formatters=custom_formatters) as pb:
            for i in pb(range(40), label=str(text)):
                time.sleep(duration)
    except Exception as e:
        logger.error(f"Error displaying progress bar: {e}")

def show_notification(message: str) -> None:
    """Show a system notification.
    
    Args:
        message: The notification message to display
    """
    try:
        notification.notify(
            title='HackerBox',
            message=message,
            app_icon=str(NOTIFICATION_ICON),
            timeout=NOTIFICATION_TIMEOUT
        )
    except Exception as e:
        logger.error(f"Error showing notification: {e}")

def make_request(url: str, auth: Optional[tuple] = None) -> requests.Response:
    """Make an HTTP request with proper error handling.
    
    Args:
        url: The URL to request
        auth: Optional tuple of (username, password) for basic auth
    
    Returns:
        Response object from the request
    
    Raises:
        RequestException: If the request fails
    """
    try:
        response = requests.get(url, auth=auth, timeout=REQUEST_TIMEOUT)
        return response
    except requests.exceptions.RequestException as e:
        logger.error(f"Request failed for {url}: {e}")
        raise

def read_wordlist(file_path: Path) -> list[str]:
    """Read and parse a wordlist file.
    
    Args:
        file_path: Path to the wordlist file
    
    Returns:
        List of strings from the file with whitespace stripped
    """
    try:
        with open(file_path) as f:
            return [line.strip() for line in f if line.strip()]
    except IOError as e:
        logger.error(f"Error reading wordlist {file_path}: {e}")
        raise