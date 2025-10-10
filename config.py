"""Configuration settings for HackerBox."""

from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent

# Dictionary paths
DICS_DIR = BASE_DIR / 'Dics'
ADMIN_PANELS_DIR = DICS_DIR / 'AdminPanels'
PASSLISTS_DIR = DICS_DIR / 'PassLists'
USERNAMES_DIR = DICS_DIR / 'UserNames'
PAYLOADS_DIR = DICS_DIR / 'PayloadsTextFiles'

# Default files
DEFAULT_ADMIN_PANELS = ADMIN_PANELS_DIR / 'admin_panels.txt'
DEFAULT_PASSLIST = PASSLISTS_DIR / '10k-most-common.txt'
DEFAULT_USERNAMES = USERNAMES_DIR / 'top-usernames-shortlist.txt'

# Notification settings
NOTIFICATION_ICON = BASE_DIR / 'Icons' / 'Appicon.ico'
NOTIFICATION_TIMEOUT = 10

# Progress bar settings
PROGRESS_BAR_STYLE = {
    'label': 'bg:#ffff00 #000000',
    'percentage': 'bg:#ffff00 #000000',
    'current': '#448844',
    'bar': ''
}

# Request settings
REQUEST_TIMEOUT = 30  # seconds

# Logging settings
LOG_FILE = BASE_DIR / 'hackerbox.log'
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# Version
VERSION = '1.0'