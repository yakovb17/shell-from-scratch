from commands.command_base import Command


class ExitCommand(Command):
    def execute(self, args) -> None:
        raise SystemExit
