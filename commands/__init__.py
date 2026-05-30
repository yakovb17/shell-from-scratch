from commands.command_base import Command
from commands.echo_command import EchoCommand
from commands.exit_command import ExitCommand
from commands.print_working_directory_command import PrintWorkingDirectoryCommand
from commands.type_command import TypeCommand

COMMANDS_NAMES_TO_CLASS: dict[str, type[Command]] = {
    "type": TypeCommand,
    "echo": EchoCommand,
    "exit": ExitCommand,
    "pwd": PrintWorkingDirectoryCommand,
}
