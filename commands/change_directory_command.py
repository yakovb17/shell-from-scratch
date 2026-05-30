import os
from pathlib import Path

from commands import Command


class ChangeDirectoryCommand(Command):
    def execute(self, args) -> None:
        path = Path(args[0])
        if os.path.exists(path):
            os.chdir(path)
        else:
            print(f"cd: {args[0]}: No such file or directory")
