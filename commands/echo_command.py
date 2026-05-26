from commands.command_base import Command


class EchoCommand(Command):
    def execute(self, args) -> None:
        print(" ".join(args))
