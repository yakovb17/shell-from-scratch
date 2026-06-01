import sys

import pytest

from utils import handle_unknown_command, get_command_and_args_from_user_input


@pytest.mark.parametrize(
    ("user_input", "expected_command", "expected_args"),
    [
        ("python -V", "python", ["-V"]),
        ("ls -la /home/user", "ls", ["-la", "/home/user"]),
        ("echo 'Hello, World!'", "echo", ["Hello, World!"]),
        ("git commit -m 'Initial commit'", "git", ["commit", "-m", "Initial commit"]),
        ("   python   -V   ", "python", ["-V"]),
        ("singlecommand", "singlecommand", []),
        ('echo "Hello, World!"', "echo", ["Hello, World!"]),
        (
            "echo \"'Hello, World! with single quote'\"",
            "echo",
            ["'Hello, World! with single quote'"],
        ),
    ],
)
def test_get_command_and_args_from_user_input(
    user_input: str, expected_command: str, expected_args: list[str]
) -> None:
    command, args = get_command_and_args_from_user_input(user_input)
    assert command == expected_command
    assert args == expected_args


def test_handle_unknown_command(capsys) -> None:
    handle_unknown_command("python", ["-V"])
    assert capsys.readouterr().out.strip() == f"Python {sys.version.split()[0]}"
