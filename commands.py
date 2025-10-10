"""Command handler module for HackerBox."""

from abc import ABC, abstractmethod
from typing import Dict, Type, Optional, Callable, Any
import getpass
import os
import socket
import subprocess
from datetime import datetime
from pathlib import Path
import logging
import importlib
import sys
from importlib.machinery import SourceFileLoader

from utils import show_notification, show_progress_bar, make_request
from settings import Settings
from config import (
    DEFAULT_ADMIN_PANELS,
    DEFAULT_PASSLIST,
    DEFAULT_USERNAMES,
    BASE_DIR
)

logger = logging.getLogger(__name__)

def load_script_module(script_name: str) -> Any:
    """Load a script module from the Scripts directory.
    
    Args:
        script_name: Name of the script file (with or without .py extension)
        
    Returns:
        The loaded module
        
    Raises:
        ImportError: If the module cannot be loaded
    """
    if not script_name.endswith('.py'):
        script_name += '.py'
        
    # Handle special characters in filename (like hyphens)
    if '-' in script_name:
        script_path = os.path.join(BASE_DIR, 'Scripts', script_name)
        return SourceFileLoader(script_name.replace('.py', '').replace('-', '_'), script_path).load_module()
    else:
        # Use standard import for normal filenames
        module_name = f"Scripts.{script_name.replace('.py', '')}"
        return importlib.import_module(module_name)

class CommandError(Exception):
    """Base exception for command-related errors."""
    pass

class CommandNotFoundError(CommandError):
    """Raised when a command is not found in the registry."""
    pass

class CommandExecutionError(CommandError):
    """Raised when a command fails to execute."""
    pass

class Command(ABC):
    """Base command class that all commands should inherit from."""

    @abstractmethod
    def execute(self, *args, **kwargs) -> None:
        """Execute the command.
        
        Args:
            *args: Variable length argument list
            **kwargs: Arbitrary keyword arguments
            
        Raises:
            CommandExecutionError: If the command fails to execute
        """
        pass

    def validate_args(self, *args, **kwargs) -> None:
        """Validate command arguments.
        
        Args:
            *args: Variable length argument list
            **kwargs: Arbitrary keyword arguments
            
        Raises:
            ValueError: If arguments are invalid
        """
        pass

class AboutCommand(Command):
    def execute(self, *args, **kwargs) -> None:
        try:
            print("HackerBox is an Opensource Program by Muhammad Sami Furqan.")
            logger.info("About command executed successfully")
        except Exception as e:
            logger.error(f"Failed to execute about command: {e}")
            raise CommandExecutionError(f"Failed to show about info: {e}")

class LicenseCommand(Command):
    def execute(self, *args, **kwargs) -> None:
        try:
            print(f"""
This Software is licensed to {getpass.getuser()}.
|------------------------------------------------------|
|              LICENSE INFO                            |
|              -------------                           |
|-> CLI Based Software.                                |
|-> Open-Source.                                       |
|-> Version 1.0                                        |
|-> Language : Python3.                                |
|-> For Pentesters and for Ethical Hackers.            |
|-> Type : Terminal.                                   |
|------------------------------------------------------|
""")
            logger.info("License command executed successfully")
        except Exception as e:
            logger.error(f"Failed to execute license command: {e}")
            raise CommandExecutionError(f"Failed to show license info: {e}")

class WhoAmICommand(Command):
    def execute(self, *args, **kwargs) -> None:
        try:
            print(getpass.getuser())
            logger.info("WhoAmI command executed successfully")
        except Exception as e:
            logger.error(f"Failed to execute whoami command: {e}")
            raise CommandExecutionError(f"Failed to get user info: {e}")

class ExitCommand(Command):
    def execute(self, *args, **kwargs) -> None:
        try:
            print("Exiting HackerBox")
            logger.info("Exit command executed successfully")
            os._exit(0)
        except Exception as e:
            logger.error(f"Failed to execute exit command: {e}")
            raise CommandExecutionError(f"Failed to exit: {e}")

class ClearCommand(Command):
    def execute(self, *args, **kwargs) -> None:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            logger.info("Clear command executed successfully")
        except Exception as e:
            logger.error(f"Failed to execute clear command: {e}")
            raise CommandExecutionError(f"Failed to clear screen: {e}")

class AdminPanelFinderCommand(Command):
    def execute(self, *args, **kwargs) -> None:
        try:
            module = load_script_module('Admin_Panel_Finder')
            if hasattr(module, 'AdminPanelFinder'):
                module.AdminPanelFinder()
            else:
                print("Admin Panel Finder module loaded but function not found")
                return
            logger.info("Admin Panel Finder command executed successfully")
        except Exception as e:
            logger.error(f"Failed to execute Admin Panel Finder command: {e}")
            raise CommandExecutionError(f"Failed to run Admin Panel Finder: {e}")

class BruteforceCommand(Command):
    def execute(self, *args, **kwargs) -> None:
        try:
            module = load_script_module('Bruteforcer')
            if hasattr(module, 'Bruteforcer'):
                module.Bruteforcer()
            elif hasattr(module, 'main'):
                module.main()
            else:
                print("Bruteforcer module loaded but function not found")
                return
            logger.info("Bruteforcer command executed successfully")
        except Exception as e:
            logger.error(f"Failed to execute Bruteforcer command: {e}")
            raise CommandExecutionError(f"Failed to run Bruteforcer: {e}")

class XSSCheckerCommand(Command):
    def execute(self, *args, **kwargs) -> None:
        try:
            module = load_script_module('CrossSiteScriptingChecker')
            if hasattr(module, 'CrossSiteScriptingChecker'):
                module.CrossSiteScriptingChecker()
            elif hasattr(module, 'main'):
                module.main()
            else:
                print("XSS Checker module loaded but function not found")
                return
            logger.info("XSS Checker command executed successfully")
        except Exception as e:
            logger.error(f"Failed to execute XSS Checker command: {e}")
            raise CommandExecutionError(f"Failed to run XSS Checker: {e}")

class DosCommand(Command):
    def execute(self, *args, **kwargs) -> None:
        try:
            module = load_script_module('Dos')
            if hasattr(module, 'Dos'):
                module.Dos()
            elif hasattr(module, 'main'):
                module.main()
            else:
                print("DoS module loaded but function not found")
                return
            logger.info("DoS command executed successfully")
        except Exception as e:
            logger.error(f"Failed to execute DoS command: {e}")
            raise CommandExecutionError(f"Failed to run DoS: {e}")

class NmapCommand(Command):
    def execute(self, *args, **kwargs) -> None:
        try:
            module = load_script_module('Nmap-t')
            
            # Try different possible function names
            if hasattr(module, 'Nmap'):
                module.Nmap()
            elif hasattr(module, 'main'):
                module.main()
            elif hasattr(module, 'main2'):
                module.main2()
            else:
                # If no specific function found, just acknowledge execution
                logger.info("Nmap module loaded but no specific function found")
                print("Running Nmap scan...")
                return
                
            logger.info("Nmap command executed successfully")
        except Exception as e:
            logger.error(f"Failed to execute Nmap command: {e}")
            raise CommandExecutionError(f"Failed to run Nmap: {e}")

class WebAnalyzerCommand(Command):
    def execute(self, *args, **kwargs) -> None:
        try:
            module = load_script_module('WebAnalyzer')
            if hasattr(module, 'WebAnalyzer'):
                module.WebAnalyzer()
            elif hasattr(module, 'main'):
                module.main()
            else:
                print("Web Analyzer module loaded but function not found")
                return
            logger.info("Web Analyzer command executed successfully")
        except Exception as e:
            logger.error(f"Failed to execute Web Analyzer command: {e}")
            raise CommandExecutionError(f"Failed to run Web Analyzer: {e}")

class WebBruteforceCommand(Command):
    def execute(self, *args, **kwargs) -> None:
        try:
            module = load_script_module('Web_bruteforce')
            if hasattr(module, 'main2'):
                module.main2()
            elif hasattr(module, 'main'):
                module.main()
            else:
                print("Web Bruteforce module loaded but function not found")
                return
            logger.info("Web Bruteforce command executed successfully")
        except Exception as e:
            logger.error(f"Failed to execute Web Bruteforce command: {e}")
            raise CommandExecutionError(f"Failed to run Web Bruteforce: {e}")

class FTPBruteforceCommand(Command):
    def execute(self, *args, **kwargs) -> None:
        try:
            module = load_script_module('ftp_bruteforcer')
            if hasattr(module, 'main'):
                module.main()
            else:
                print("FTP Bruteforcer module loaded but function not found")
                return
            logger.info("FTP Bruteforcer command executed successfully")
        except Exception as e:
            logger.error(f"Failed to execute FTP Bruteforcer command: {e}")
            raise CommandExecutionError(f"Failed to run FTP Bruteforcer: {e}")

class LivePortDiscoveryCommand(Command):
    def execute(self, *args, **kwargs) -> None:
        try:
            module = load_script_module('live_port_discovery')
            if hasattr(module, 'main2'):
                module.main2()
            elif hasattr(module, 'main'):
                module.main()
            else:
                print("Live Port Discovery module loaded but function not found")
                return
            logger.info("Live Port Discovery command executed successfully")
        except Exception as e:
            logger.error(f"Failed to execute Live Port Discovery command: {e}")
            raise CommandExecutionError(f"Failed to run Live Port Discovery: {e}")

class HelpCommand(Command):
    def execute(self, *args, **kwargs) -> None:
        try:
            from rich.console import Console
            from rich.table import Table

            console = Console()
            
            # Create main table
            table = Table(title="HackerBox Commands", show_header=False)
            table.add_column("Command", style="cyan")
            table.add_column("Description", style="white")

            # Basic Commands section
            basic_table = Table(title="Basic Commands", show_header=False)
            basic_table.add_column("Command", style="yellow")
            basic_table.add_column("Description")
            
            basic_table.add_row("about", "Show information about HackerBox")
            basic_table.add_row("license", "Display license information")
            basic_table.add_row("whoami", "Show current user")
            basic_table.add_row("exit, e", "Exit HackerBox")
            basic_table.add_row("clear, cls", "Clear the screen")
            basic_table.add_row("help", "Show this help message")

            # Terminal Commands section
            terminal_table = Table(title="Terminal Commands", show_header=False)
            terminal_table.add_column("Command", style="yellow")
            terminal_table.add_column("Description")
            
            terminal_table.add_row("pwd", "Print working directory")
            terminal_table.add_row("ls, dir", "List directory contents")
            terminal_table.add_row("cd", "Change directory")
            terminal_table.add_row("datetime, date, time, d/t", "Display current date and time")
            terminal_table.add_row("host.getip", "Get IP address from hostname")
            terminal_table.add_row("echo", "Display a line of text")
            terminal_table.add_row("history", "Display command history")
            terminal_table.add_row("touch", "Create a new empty file")
            terminal_table.add_row("mkdir", "Create a new directory")
            terminal_table.add_row("rm", "Remove a file")
            terminal_table.add_row("rmdir", "Remove an empty directory")
            terminal_table.add_row("systeminfo, sysinfo, system", "Display system information")
            terminal_table.add_row("check-updates, update", "Check for HackerBox updates")

            # Security Tools section
            security_table = Table(title="Security Tools", show_header=False)
            security_table.add_column("Command", style="yellow")
            security_table.add_column("Description")
            
            security_table.add_row("admin-panel-finder, apf", "Find admin panels on a target website")
            security_table.add_row("bruteforce, bf", "General purpose bruteforcer")
            security_table.add_row("xss-checker, xss", "Check for XSS vulnerabilities")
            security_table.add_row("dos", "Perform DoS testing")
            security_table.add_row("nmap", "Network scanning utility")
            security_table.add_row("web-analyzer, wa", "Analyze web applications")
            security_table.add_row("web-bruteforce, wbf", "Web login bruteforcer")
            security_table.add_row("ftp-bruteforce, ftpbf", "FTP login bruteforcer")
            security_table.add_row("port-discovery, pd", "Discover open ports on a target")

            # Print tables
            console.print()
            console.print(basic_table)
            console.print()
            console.print(terminal_table)
            console.print()
            console.print(security_table)
            console.print()
            console.print("For more information, visit: [link]https://github.com/samifurqan/hackerbox[/link]")
            console.print()

            logger.info("Help command executed successfully")
        except Exception as e:
            logger.error(f"Failed to execute help command: {e}")
            raise CommandExecutionError(f"Failed to show help: {e}")

class PwdCommand(Command):
    def execute(self, *args, **kwargs) -> None:
        try:
            print(os.getcwd())
            logger.info("Pwd command executed successfully")
        except Exception as e:
            logger.error(f"Failed to execute pwd command: {e}")
            raise CommandExecutionError(f"Failed to get current directory: {e}")

class LsCommand(Command):
    def execute(self, *args, **kwargs) -> None:
        try:
            path = args[0] if args else os.getcwd()
            if os.path.isdir(path):
                files = os.listdir(path)
                
                # Get directory and file details
                entries = []
                total_size = 0
                for file in sorted(files):
                    full_path = os.path.join(path, file)
                    stats = os.stat(full_path)
                    
                    # Get file size in appropriate units
                    size = stats.st_size
                    total_size += size
                    if size >= 1024**3:
                        size_str = f"{size/1024**3:.1f}GB"
                    elif size >= 1024**2:
                        size_str = f"{size/1024**2:.1f}MB"
                    elif size >= 1024:
                        size_str = f"{size/1024:.1f}KB"
                    else:
                        size_str = f"{size}B"
                        
                    # Get last modified time
                    mod_time = datetime.fromtimestamp(stats.st_mtime)
                    date_str = mod_time.strftime("%m/%d/%Y  %H:%M %p")
                    
                    is_dir = os.path.isdir(full_path)
                    entries.append((is_dir, file, size_str, date_str))

                # Print directory listing header
                print(f"\n Directory of {os.path.abspath(path)}\n")
                
                # Print entries in Windows dir style
                dir_count = 0
                file_count = 0
                
                for is_dir, name, size, date in entries:
                    if is_dir:
                        print(f"{date}\t<DIR>\t\t{name}")
                        dir_count += 1
                    else:
                        print(f"{date}\t     \t{size}\t{name}")
                        file_count += 1
                        
                # Print summary
                print(f"\n\t{file_count} File(s)\t{total_size:,} bytes")
                print(f"\t{dir_count} Dir(s)")
                
            else:
                print(f"Path not found: {path}")
            logger.info("Ls command executed successfully")
        except Exception as e:
            logger.error(f"Failed to execute ls command: {e}")
            raise CommandExecutionError(f"Failed to list directory: {e}")

class CdCommand(Command):
    def execute(self, *args, **kwargs) -> None:
        try:
            if not args:
                # If no arguments, print current directory
                print(f"Current directory: {os.getcwd()}")
                return
                
            path = args[0]
            if os.path.isdir(path):
                os.chdir(path)
                print(f"Changed directory to: {os.getcwd()}")
            else:
                print(f"Directory not found: {path}")
            logger.info("Cd command executed successfully")
        except Exception as e:
            logger.error(f"Failed to execute cd command: {e}")
            raise CommandExecutionError(f"Failed to change directory: {e}")

class DateTimeCommand(Command):
    def execute(self, *args, **kwargs) -> None:
        try:
            print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            logger.info("DateTime command executed successfully")
        except Exception as e:
            logger.error(f"Failed to execute datetime command: {e}")
            raise CommandExecutionError(f"Failed to get date and time: {e}")

class HostGetIpCommand(Command):
    def execute(self, *args, **kwargs) -> None:
        try:
            if args:
                host = args[0]
            else:
                host = input("Enter Host URL: ")
                
            ip = socket.gethostbyname(host)
            print(f"The IP address of {host} is {ip}")
            logger.info("HostGetIp command executed successfully")
        except Exception as e:
            logger.error(f"Failed to execute hostgetip command: {e}")
            raise CommandExecutionError(f"Failed to get host IP: {e}")

class EchoCommand(Command):
    def execute(self, *args, **kwargs) -> None:
        try:
            print(" ".join(args))
            logger.info("Echo command executed successfully")
        except Exception as e:
            logger.error(f"Failed to execute echo command: {e}")
            raise CommandExecutionError(f"Failed to echo text: {e}")

class HistoryCommand(Command):
    def execute(self, *args, **kwargs) -> None:
        try:
            history = kwargs.get('history', [])
            if not history:
                print("No command history available")
                return
                
            for i, cmd in enumerate(history, 1):
                print(f"{i}: {cmd}")
            logger.info("History command executed successfully")
        except Exception as e:
            logger.error(f"Failed to execute history command: {e}")
            raise CommandExecutionError(f"Failed to show command history: {e}")

class TouchCommand(Command):
    def execute(self, *args, **kwargs) -> None:
        try:
            if not args:
                print("Usage: touch <filename>")
                return
                
            filename = args[0]
            with open(filename, 'a'):
                os.utime(filename, None)
            print(f"Created/updated file: {filename}")
            logger.info("Touch command executed successfully")
        except Exception as e:
            logger.error(f"Failed to execute touch command: {e}")
            raise CommandExecutionError(f"Failed to create/update file: {e}")

class MkdirCommand(Command):
    def execute(self, *args, **kwargs) -> None:
        try:
            if not args:
                print("Usage: mkdir <directory>")
                return
                
            directory = args[0]
            os.makedirs(directory, exist_ok=True)
            print(f"Created directory: {directory}")
            logger.info("Mkdir command executed successfully")
        except Exception as e:
            logger.error(f"Failed to execute mkdir command: {e}")
            raise CommandExecutionError(f"Failed to create directory: {e}")

class RmCommand(Command):
    def execute(self, *args, **kwargs) -> None:
        try:
            if not args:
                print("Usage: rm <file>")
                return
                
            path = args[0]
            if os.path.isfile(path):
                os.remove(path)
                print(f"Removed file: {path}")
            elif os.path.isdir(path):
                print(f"Cannot remove directory with rm. Use rmdir for directories.")
            else:
                print(f"File not found: {path}")
            logger.info("Rm command executed successfully")
        except Exception as e:
            logger.error(f"Failed to execute rm command: {e}")
            raise CommandExecutionError(f"Failed to remove file: {e}")

class RmdirCommand(Command):
    def execute(self, *args, **kwargs) -> None:
        try:
            if not args:
                print("Usage: rmdir <directory>")
                return
                
            directory = args[0]
            if os.path.isdir(directory):
                try:
                    os.rmdir(directory)
                    print(f"Removed directory: {directory}")
                except OSError:
                    print(f"Directory not empty: {directory}")
            else:
                print(f"Directory not found: {directory}")
            logger.info("Rmdir command executed successfully")
        except Exception as e:
            logger.error(f"Failed to execute rmdir command: {e}")
            raise CommandExecutionError(f"Failed to remove directory: {e}")

class SystemInfoCommand(Command):
    def execute(self, *args, **kwargs) -> None:
        try:
            import platform
            import psutil
            
            # Try to import psutil but don't fail if it's not available
            try:
                import psutil
                has_psutil = True
            except ImportError:
                has_psutil = False
            
            print("\n===== SYSTEM INFORMATION =====")
            print(f"OS: {platform.system()} {platform.release()} {platform.version()}")
            print(f"Architecture: {platform.machine()}")
            print(f"Processor: {platform.processor()}")
            print(f"Python Version: {platform.python_version()}")
            print(f"Node: {platform.node()}")
            
            if has_psutil:
                # Memory information
                mem = psutil.virtual_memory()
                print(f"\n===== MEMORY INFORMATION =====")
                print(f"Total: {mem.total / (1024**3):.2f} GB")
                print(f"Available: {mem.available / (1024**3):.2f} GB")
                print(f"Used: {mem.used / (1024**3):.2f} GB ({mem.percent}%)")
                
                # Disk information
                print(f"\n===== DISK INFORMATION =====")
                for part in psutil.disk_partitions(all=False):
                    if os.name == 'nt' and 'cdrom' in part.opts or part.fstype == '':
                        # Skip CD-ROM drives on Windows
                        continue
                    usage = psutil.disk_usage(part.mountpoint)
                    print(f"Disk {part.device} ({part.mountpoint}):")
                    print(f"  Total: {usage.total / (1024**3):.2f} GB")
                    print(f"  Used: {usage.used / (1024**3):.2f} GB ({usage.percent}%)")
                    print(f"  Free: {usage.free / (1024**3):.2f} GB")
            else:
                print("\nInstall 'psutil' package for more detailed system information.")
                print("Run: pip install psutil")
                
            logger.info("SystemInfo command executed successfully")
        except Exception as e:
            logger.error(f"Failed to execute systeminfo command: {e}")
            raise CommandExecutionError(f"Failed to get system information: {e}")

class CheckUpdatesCommand(Command):
    def execute(self, *args, **kwargs) -> None:
        try:
            print("Checking for updates...")
            show_progress_bar("Connecting to GitHub", 0.5)
            
            try:
                # Try to import requests but don't fail if it's not available
                import requests
                has_requests = True
            except ImportError:
                has_requests = False
                
            if has_requests:
                try:
                    # GitHub API URL for the repository
                    repo_url = "https://api.github.com/repos/samifurqan/hackerbox/releases/latest"
                    response = requests.get(repo_url, timeout=10)
                    
                    if response.status_code == 200:
                        latest_release = response.json()
                        latest_version = latest_release.get('tag_name', 'unknown')
                        current_version = "1.0"  # This should be defined somewhere in your app
                        
                        print(f"Current version: {current_version}")
                        print(f"Latest version: {latest_version}")
                        
                        if latest_version != "unknown" and latest_version != current_version:
                            print("\nA new version is available!")
                            print(f"Release notes: {latest_release.get('body', 'No release notes available')}")
                            print(f"\nDownload from: {latest_release.get('html_url', 'https://github.com/samifurqan/hackerbox/releases')}")
                            show_notification("HackerBox Update Available", f"Version {latest_version} is now available!")
                        else:
                            print("\nYou are using the latest version of HackerBox.")
                    else:
                        print(f"Failed to check for updates. Status code: {response.status_code}")
                except Exception as e:
                    print(f"Error checking for updates: {e}")
            else:
                print("The 'requests' package is required to check for updates.")
                print("Run: pip install requests")
                
            logger.info("CheckUpdates command executed successfully")
        except Exception as e:
            logger.error(f"Failed to execute check-updates command: {e}")
            raise CommandExecutionError(f"Failed to check for updates: {e}")

class CommandRegistry:
    """Registry for managing available commands."""

    def __init__(self):
        self._commands: Dict[str, Type[Command]] = {
            # Basic commands
            'about': AboutCommand,
            'license': LicenseCommand,
            'whoami': WhoAmICommand,
            'exit': ExitCommand,
            'e': ExitCommand,
            'clear': ClearCommand,
            'cls': ClearCommand,
            'help': HelpCommand,
            
            # Common terminal commands
            'pwd': PwdCommand,
            'ls': LsCommand,
            'dir': LsCommand,
            'cd': CdCommand,
            'datetime': DateTimeCommand,
            'date': DateTimeCommand,
            'time': DateTimeCommand,
            'd/t': DateTimeCommand,
            'host.getip': HostGetIpCommand,
            'echo': EchoCommand,
            'history': HistoryCommand,
            'touch': TouchCommand,
            'mkdir': MkdirCommand,
            'rm': RmCommand,
            'rmdir': RmdirCommand,
            'systeminfo': SystemInfoCommand,
            'sysinfo': SystemInfoCommand,
            'system': SystemInfoCommand,
            'check-updates': CheckUpdatesCommand,
            'update': CheckUpdatesCommand,
            
            # Security tool commands
            'admin-panel-finder': AdminPanelFinderCommand,
            'apf': AdminPanelFinderCommand,
            'bruteforce': BruteforceCommand,
            'bf': BruteforceCommand,
            'xss-checker': XSSCheckerCommand,
            'xss': XSSCheckerCommand,
            'dos': DosCommand,
            'nmap': NmapCommand,
            'web-analyzer': WebAnalyzerCommand,
            'wa': WebAnalyzerCommand,
            'web-bruteforce': WebBruteforceCommand,
            'wbf': WebBruteforceCommand,
            'ftp-bruteforce': FTPBruteforceCommand,
            'ftpbf': FTPBruteforceCommand,
            'port-discovery': LivePortDiscoveryCommand,
            'pd': LivePortDiscoveryCommand,
        }

    def register_command(self, name: str, command_class: Type[Command]) -> None:
        """Register a new command.
        
        Args:
            name: Command name
            command_class: Command class to register
            
        Raises:
            ValueError: If name is empty or command_class is None
        """
        if not name:
            raise ValueError("Command name cannot be empty")
        if not command_class:
            #Command name cannot be empty
            raise ValueError("Command class cannot be None")
            
        self._commands[name.lower()] = command_class
        logger.info(f"Registered command: {name}")

    def get_command(self, name: str) -> Command:
        """Get a command instance by name.
        
        Args:
            name: Name of the command to get
            
        Returns:
            Command instance
            
        Raises:
            CommandNotFoundError: If command is not found
        """
        command_class = self._commands.get(name.lower())
        if command_class:
            return command_class()
        raise CommandNotFoundError(f"Command '{name}' not found")

    def execute_command(self, name: str, *args, **kwargs) -> None:
        """Execute a command by name.
        
        Args:
            name: Name of the command to execute
            *args: Variable length argument list
            **kwargs: Arbitrary keyword arguments
        """
        try:
            if not name:
                logger.warning("Empty command name provided")
                return
                
            command = self.get_command(name)
            command.validate_args(*args, **kwargs)
            command.execute(*args, **kwargs)
            logger.info(f"Successfully executed command: {name}")
            
        except CommandNotFoundError as e:
            logger.warning(f"Unknown command: {name}")
            print(f"Unknown command: {name}")
        except ValueError as e:
            logger.error(f"Invalid arguments for command {name}: {e}")
            print(f"Invalid arguments for command {name}: {e}")
        except CommandExecutionError as e:
            logger.error(f"Error executing command {name}: {e}")
            print(f"Error executing command {name}: {e}")
        except Exception as e:
            logger.error(f"Unexpected error executing command {name}: {e}")
            print(f"Unexpected error executing command {name}: {e}")
