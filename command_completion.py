"""Command completion module for HackerBox."""

from typing import List, Dict, Iterable, Optional, Tuple
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.document import Document

class HackerBoxCompleter(Completer):
    """Command completer for HackerBox.
    
    This completer provides suggestions for available commands in the HackerBox
    terminal based on the CommandRegistry.
    """
    
    def __init__(self, command_registry):
        """Initialize the completer with a command registry.
        
        Args:
            command_registry: The CommandRegistry instance containing available commands
        """
        self.command_registry = command_registry
        self.command_descriptions = {
            # Basic commands
            'about': 'Show information about HackerBox',
            'license': 'Display license information',
            'whoami': 'Show current user',
            'exit': 'Exit HackerBox',
            'e': 'Exit HackerBox (shortcut)',
            'clear': 'Clear the screen',
            'cls': 'Clear the screen (shortcut)',
            'help': 'Show help message',
            
            # Common terminal commands
            'pwd': 'Print working directory',
            'ls': 'List directory contents',
            'dir': 'List directory contents (alias for ls)',
            'cd': 'Change directory',
            'datetime': 'Display current date and time',
            'date': 'Display current date and time (alias for datetime)',
            'time': 'Display current date and time (alias for datetime)',
            'd/t': 'Display current date and time (shortcut)',
            'host.getip': 'Get IP address from hostname',
            'echo': 'Display a line of text',
            'history': 'Display command history',
            'touch': 'Create a new empty file',
            'mkdir': 'Create a new directory',
            'rm': 'Remove a file',
            'rmdir': 'Remove an empty directory',
            'systeminfo': 'Display system information',
            'sysinfo': 'Display system information (alias for systeminfo)',
            'system': 'Display system information (alias for systeminfo)',
            'check-updates': 'Check for HackerBox updates',
            'update': 'Check for HackerBox updates (alias for check-updates)',
            
            # Security tool commands
            'admin-panel-finder': 'Find admin panels on a target website',
            'apf': 'Find admin panels (shortcut)',
            'bruteforce': 'General purpose bruteforcer',
            'bf': 'General purpose bruteforcer (shortcut)',
            'xss-checker': 'Check for XSS vulnerabilities',
            'xss': 'Check for XSS vulnerabilities (shortcut)',
            'dos': 'Perform DoS testing',
            'nmap': 'Network scanning utility',
            'web-analyzer': 'Analyze web applications',
            'wa': 'Analyze web applications (shortcut)',
            'web-bruteforce': 'Web login bruteforcer',
            'wbf': 'Web login bruteforcer (shortcut)',
            'ftp-bruteforce': 'FTP login bruteforcer',
            'ftpbf': 'FTP login bruteforcer (shortcut)',
            'port-discovery': 'Discover open ports on a target',
            'pd': 'Discover open ports (shortcut)'
        }
        
    def get_completions(self, document: Document, complete_event) -> Iterable[Completion]:
        """Get command completions based on current input.
        
        Args:
            document: The Document instance containing the current input
            complete_event: The completion event
            
        Returns:
            Iterable of Completion objects
        """
        text = document.text_before_cursor.lstrip()
        
        # If no text, suggest all commands
        if not text:
            for cmd_name, description in self._get_commands_with_descriptions():
                yield Completion(cmd_name, start_position=0, display=cmd_name, display_meta=description)
            return
        
        # Check if we're completing a command
        if ' ' not in text:  # No space means we're still typing the command
            for cmd_name, description in self._get_commands_with_descriptions():
                if cmd_name.startswith(text):
                    yield Completion(cmd_name, start_position=-len(text), display=cmd_name, display_meta=description)
    
    def _get_command_names(self) -> List[str]:
        """Get all available command names from the registry.
        
        Returns:
            List of command names
        """
        # Access the private _commands dictionary from the registry
        if hasattr(self.command_registry, '_commands'):
            return sorted(self.command_registry._commands.keys())
        return []
    
    def _get_commands_with_descriptions(self) -> List[Tuple[str, str]]:
        """Get all available commands with their descriptions.
        
        Returns:
            List of tuples containing (command_name, description)
        """
        commands = []
        for cmd_name in self._get_command_names():
            description = self.command_descriptions.get(cmd_name, '')
            commands.append((cmd_name, description))
        return sorted(commands)