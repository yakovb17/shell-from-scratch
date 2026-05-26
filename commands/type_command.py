import os
import stat
from pathlib import Path
from commands.command_base import Command


class TypeCommand(Command):
    def __init__(
        self, command_registry: dict[str, type[Command]], *args, **kwargs
    ) -> None:
        self.command_registry = command_registry

    def execute(self, args) -> None:
        command = args[0]
        if command in self.command_registry:
            print(f"{command} is a shell builtin")
        elif full_path := self._check_command_exists_as_file(command):
            print(f"{command} is {full_path}")
        else:
            print(f"{command}: not found")

    def _check_command_exists_as_file(self, command: str) -> Path | None:
        if (env_path := os.environ.get("PATH")) is None:
            return None

        for dir_path in env_path.split(os.pathsep):
            for root, dirs, files in os.walk(dir_path):
                if command in files and (
                    full_path := self._check_file_have_execute_permission(
                        Path(root) / command
                    )
                ):
                    return full_path
        return None

    @staticmethod
    def _check_file_have_execute_permission(file_path: Path) -> Path | None:
        file_mode = os.stat(file_path).st_mode
        for permission in (stat.S_IXUSR, stat.S_IXGRP, stat.S_IXOTH):
            if bool(file_mode & permission):
                return file_path
        return None
