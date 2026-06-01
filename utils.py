import re
import subprocess
from commands import TypeCommand


def _parse_command_args(args_str: str) -> list[str]:
    return [
        match.group(1) or match.group(2)
        for match in re.finditer(r"'([^']*)'|(\S+)", args_str.replace("''", ""))
    ]


def get_command_and_args_from_user_input(user_input: str) -> tuple[str, list[str]]:
    split_input = user_input.strip().split(" ", 1)
    command = split_input[0].strip()
    args = split_input[1] if len(split_input) > 1 else ""

    return command, _parse_command_args(args)


def handle_unknown_command(user_command: str, command_args: list[str]) -> None:
    if TypeCommand.find_command_executable_file(user_command):
        res = subprocess.run([user_command, *command_args], capture_output=True)
        print(res.stdout.decode().strip())
    else:
        print(f"{user_command}: command not found")
