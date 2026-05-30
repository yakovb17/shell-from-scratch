import sys

from commands import EchoCommand, ExitCommand, TypeCommand, COMMANDS_NAMES_TO_CLASS
import pytest

from commands.utils import handle_unknown_command


def test_echo_command(capsys) -> None:
    command_args = "test echo"
    EchoCommand().execute([command_args])
    assert capsys.readouterr().out.strip() == command_args


def test_exit_command() -> None:
    with pytest.raises(SystemExit):
        ExitCommand().execute([])


@pytest.mark.parametrize(
    ("command_name", "expected_output"),
    [
        ("echo", "echo is a shell builtin"),
        ("nonexistent_command", "nonexistent_command: not found"),
        ("ls", f"ls is {TypeCommand.find_command_executable_file('ls')}"),
    ],
)
def test_type_command_with_builtin_command(
    command_name, expected_output, capsys
) -> None:
    TypeCommand(COMMANDS_NAMES_TO_CLASS).execute([command_name])
    assert capsys.readouterr().out.strip() == expected_output

def test_handle_unknown_command(capsys) -> None:
    handle_unknown_command("python", ["-V"])
    assert capsys.readouterr().out.strip() == f"Python {sys.version.split()[0]}"
