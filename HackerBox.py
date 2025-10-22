import time
import os
import logging

# Make plumbum import optional
try:
    from plumbum import colors
except ImportError:
    # Create a simple fallback for colors if plumbum is not available
    class DummyColors:
        def __getattr__(self, name):
            return lambda text: text  # Return the text unchanged

    colors = DummyColors()
from prompt_toolkit.shortcuts import ProgressBar, prompt
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.styles import Style
from prompt_toolkit.shortcuts.progress_bar import formatters
from prompt_toolkit.history import InMemoryHistory

# Make plyer import optional with a fallback notification function
try:
    from plyer import notification

    has_notification = True
except ImportError:
    has_notification = False

# Import command completion
from command_completion import HackerBoxCompleter
from settings import SettingsManager

# Define style for progress bar
style = Style.from_dict(
    {
        "label": "bg:#ansiblue #ansiwhite",
        "percentage": "bg:#ansiblue #ansiwhite",
        "current": "#ansigreen",
        "bar": "",
    }
)

# Custom formatters for progress bar
custom_formatters = [
    formatters.Label(),
    formatters.Text(" [", style="class:percentage"),
    formatters.Percentage(),
    formatters.Text("]", style="class:percentage"),
    formatters.Text(" "),
    formatters.Bar(sym_a="#", sym_b="#", sym_c="."),
    formatters.Text("  "),
]


def show_progress(texttoshow, timee):
    with ProgressBar(style=style, formatters=custom_formatters) as pb:
        for i in pb(range(40), label=str(texttoshow)):
            time.sleep(timee)


def notification_c(fmessage):
    try:
        if has_notification:
            notification.notify(
                title="HackerBox",
                message=fmessage,
                app_icon="Icons\\Appicon.ico",
                timeout=10,
            )
        else:
            # Fallback to console output if notification module is not available
            print(f"[NOTIFICATION] {fmessage}")
    except Exception as e:
        logger = logging.getLogger(__name__)
        logger.error(f"Notification error: {e}")
        pass


from commands import CommandRegistry, CommandNotFoundError
import traceback


class HackerBox:
    def __init__(self):
        self.command_registry = CommandRegistry()
        self.logger = logging.getLogger(__name__)
        self.settings_manager = SettingsManager()
        self.settings_manager.load_settings()
        self.settings = self.settings_manager.get_settings()
        self.command_history = InMemoryHistory()
        self.completer = HackerBoxCompleter(self.command_registry)

    def usercommand(self, command=None):
        try:
            # Use command parameter if provided, otherwise check for z attribute
            if command:
                z = command
            elif hasattr(self, "z") and self.z:
                z = self.z
            else:
                self.logger.warning("No command provided")
                return

            # Split the command into parts for argument handling
            parts = z.strip().split()
            cmd_name = parts[0] if parts else ""
            args = parts[1:] if len(parts) > 1 else []

            # Special handling for history command to pass the command history
            if cmd_name == "history":
                # Convert history entries to a list
                history_list = [entry for entry in self.command_history.get_strings()]
                self.command_registry.execute_command(
                    cmd_name, *args, history=history_list
                )
                return

            # Try to use command registry for all other commands
            try:
                self.command_registry.execute_command(cmd_name, *args)
                return
            except CommandNotFoundError:
                # Fall back to legacy command handling
                self.logger.info(
                    f"Command '{cmd_name}' not found in registry, using legacy handling"
                )
                print(f"Unknown command: {cmd_name}")
                self.logger.warning(f"Unknown command attempted: {cmd_name}")
        except Exception as e:
            print(f"Error executing command: {e}")
            self.logger.error(f"Error in usercommand: {e}")
            traceback.print_exc()


# Add this at the end of the file
if __name__ == "__main__":
    # Set up basic logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        filename="hackerbox.log",
    )

    # Create an instance of HackerBox
    hb = HackerBox()

    print("Hacker Box")
    print("Copyright (c). All Rights Reserved.")
    print("Acitve Internet connection is reqired to run things properly.")

    # Main command loop
    while True:
        try:
            # Get user input with command completion if enabled
            if hb.settings.prompt_autocomplete:
                user_input = prompt(
                    "HackerBox> ",
                    history=hb.command_history,
                    completer=hb.completer,
                    complete_while_typing=True,
                )
            else:
                # Fall back to standard input if autocomplete is disabled
                user_input = input("HackerBox> ")

            # Set the input to the z attribute and execute the command
            hb.z = user_input
            hb.usercommand()
        except KeyboardInterrupt:
            print("\nExiting HackerBox...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            logging.error(f"Main loop error: {e}")
            traceback.print_exc()
