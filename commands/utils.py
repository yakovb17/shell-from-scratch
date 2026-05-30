import subprocess

from commands import TypeCommand


def handle_unknown_command(user_command: str, command_args: list[str]) -> None:
    if cmd_executable_file_path := TypeCommand.find_command_executable_file(
        user_command
    ):
        res = subprocess.run(
            [str(cmd_executable_file_path), *command_args], capture_output=True
        )
        print(res.stdout.decode().strip())
    else:
        print(f"{user_command}: command not found")
