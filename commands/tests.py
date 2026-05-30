import os
from pathlib import Path
from unittest.mock import patch

from commands import (
    EchoCommand,
    ExitCommand,
    TypeCommand,
    COMMANDS_NAMES_TO_CLASS,
    PrintWorkingDirectoryCommand,
)
import pytest

from commands.change_directory_command import ChangeDirectoryCommand


def test_echo_command(capsys: pytest.CaptureFixture[str]) -> None:
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
    command_name: str, expected_output: str, capsys: pytest.CaptureFixture[str]
) -> None:
    TypeCommand(COMMANDS_NAMES_TO_CLASS).execute([command_name])
    assert capsys.readouterr().out.strip() == expected_output


def test_pwd_command(capsys: pytest.CaptureFixture[str]) -> None:
    PrintWorkingDirectoryCommand().execute([])
    assert capsys.readouterr().out.strip() == os.getcwd()


def test_cd_command(capsys: pytest.CaptureFixture[str]) -> None:
    target_dir = Path(os.getcwd(), "commands")
    with patch("os.chdir") as mock_chdir:
        ChangeDirectoryCommand().execute([target_dir])
    assert capsys.readouterr().out.strip() == ""
    mock_chdir.assert_called_once_with(target_dir)


def test_cd_command_with_nonexistent_directory(
    capsys: pytest.CaptureFixture[str],
) -> None:
    current_dir = os.getcwd()
    target_dir = Path(current_dir, "nonexistent_directory")
    ChangeDirectoryCommand().execute([target_dir])
    assert (
        capsys.readouterr().out.strip()
        == f"cd: {target_dir}: No such file or directory"
    )
    assert os.getcwd() == current_dir
