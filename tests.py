import sys

from utils import handle_unknown_command, get_command_and_args_from_user_input


def test_get_command_and_args_from_user_input() -> None:
    command, args = get_command_and_args_from_user_input("python -V")
    assert command == "python"
    assert args == ["-V"]


def test_handle_unknown_command(capsys) -> None:
    handle_unknown_command("python", ["-V"])
    assert capsys.readouterr().out.strip() == f"Python {sys.version.split()[0]}"
