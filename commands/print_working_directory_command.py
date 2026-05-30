import os

from commands import Command


class PrintWorkingDirectoryCommand(Command):
    def execute(self, args) -> None:
        print(os.getcwd())
