"""Settings management module for HackerBox."""

import os
from pathlib import Path
from typing import Any, Dict
import configparser
from dataclasses import dataclass
import logging

from config import BASE_DIR

logger = logging.getLogger(__name__)

@dataclass
class Settings:
    """Settings data class to store configuration values."""
    # Main settings
    auto_update: bool = True
    ask_for_administrator: bool = True
    show_disclaimer: bool = True
    auto_file_sort: bool = True

    # Commands configuration
    custom_package_download_directory: str = 'Default'
    github_clone_directory: str = 'nil'

    # Youtube settings
    videos_output_directory: str = '.'
    audio_output_directory: str = '.'

    # Commandline settings
    prompt_autocomplete: bool = True
    show_errors_log: bool = False

class SettingsManager:
    """Manages application settings using configparser."""

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.settings_file = BASE_DIR / 'Settings.ini'
        self.settings = Settings()

    def write_default_settings(self) -> None:
        """Write default settings to the config file."""
        self.config['DEFAULT'] = {
            'File-Type': 'Settings',
            'Name': 'HackerBox',
            'Description': 'Settings File for HackerBox - Editable.',
            'Warning': 'Only Change this if you know what are you doing!'
        }

        self.config['Main Settings'] = {
            'Auto-Update': str(self.settings.auto_update),
            'Ask-For-Administrator': str(self.settings.ask_for_administrator),
            'Show-Disclaimer': str(self.settings.show_disclaimer),
            'Auto-File-Sort': str(self.settings.auto_file_sort)
        }

        self.config['Commands Configuration'] = {
            'Custom-Package-Download-Directory': self.settings.custom_package_download_directory,
            'GitHub-Clone-Directory': self.settings.github_clone_directory
        }

        self.config['Youtube Settings'] = {
            'Videos-Output-Directory': self.settings.videos_output_directory,
            'Audio-Output-Directory': self.settings.audio_output_directory
        }

        self.config['Commandline Settings'] = {
            'Prompt-autocomplete': str(self.settings.prompt_autocomplete),
            'Show-Errors-log': str(self.settings.show_errors_log)
        }

        try:
            with open(self.settings_file, 'w') as configfile:
                self.config.write(configfile)
            logger.info('Settings file written successfully')
        except IOError as e:
            logger.error(f'Failed to write settings file: {e}')
            raise

    def load_settings(self) -> None:
        """Load settings from the config file."""
        if not self.settings_file.exists():
            logger.warning('Settings file not found, creating default settings')
            self.write_default_settings()
            return

        try:
            self.config.read(self.settings_file)
            
            # Main Settings
            self.settings.auto_update = self.config.getboolean('Main Settings', 'Auto-Update', fallback=True)
            self.settings.ask_for_administrator = self.config.getboolean('Main Settings', 'Ask-For-Administrator', fallback=True)
            self.settings.show_disclaimer = self.config.getboolean('Main Settings', 'Show-Disclaimer', fallback=True)
            self.settings.auto_file_sort = self.config.getboolean('Main Settings', 'Auto-File-Sort', fallback=True)

            # Commands Configuration
            self.settings.custom_package_download_directory = self.config.get(
                'Commands Configuration', 'Custom-Package-Download-Directory', fallback='Default')
            self.settings.github_clone_directory = self.config.get(
                'Commands Configuration', 'GitHub-Clone-Directory', fallback='nil')

            # Youtube Settings
            self.settings.videos_output_directory = self.config.get(
                'Youtube Settings', 'Videos-Output-Directory', fallback='.')
            self.settings.audio_output_directory = self.config.get(
                'Youtube Settings', 'Audio-Output-Directory', fallback='.')

            # Commandline Settings
            self.settings.prompt_autocomplete = self.config.getboolean(
                'Commandline Settings', 'Prompt-autocomplete', fallback=True)
            self.settings.show_errors_log = self.config.getboolean(
                'Commandline Settings', 'Show-Errors-log', fallback=False)

            logger.info('Settings loaded successfully')
        except configparser.Error as e:
            logger.error(f'Failed to load settings: {e}')
            raise

    def get_settings(self) -> Settings:
        """Get the current settings."""
        return self.settings

    def update_setting(self, section: str, key: str, value: Any) -> None:
        """Update a specific setting value.

        Args:
            section: The section name in the config file
            key: The setting key to update
            value: The new value to set
        """
        try:
            self.config[section][key] = str(value)
            with open(self.settings_file, 'w') as configfile:
                self.config.write(configfile)
            logger.info(f'Updated setting {section}.{key} to {value}')
            self.load_settings()  # Reload settings after update
        except Exception as e:
            logger.error(f'Failed to update setting {section}.{key}: {e}')
            raise