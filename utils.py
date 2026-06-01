import subprocess
import shlex

from commands import TypeCommand


def get_command_and_args_from_user_input(user_input: str) -> tuple[str, list[str]]:
    split_input = user_input.strip().split(" ", 1)
    command = split_input[0].strip()
    args = shlex.split(split_input[1]) if len(split_input) > 1 else []
    return command, args


def handle_unknown_command(user_command: str, command_args: list[str]) -> None:
    if TypeCommand.find_command_executable_file(user_command):
        res = subprocess.run([user_command, *command_args], capture_output=True)
        print(res.stdout.decode().strip())
    else:
        print(f"{user_command}: command not found")
