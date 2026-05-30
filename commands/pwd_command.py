import os

from commands import Command


class PWDCommand(Command):
    def execute(self, args) -> None:
        print(os.getcwd())
