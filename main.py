from commands import COMMANDS_NAMES_TO_CLASS
from utils import get_command_and_args_from_user_input, handle_unknown_command


def main():
    while True:
        user_input = input("$ ")
        command, args = get_command_and_args_from_user_input(user_input)
        command_cls = COMMANDS_NAMES_TO_CLASS.get(command)
        if not command_cls:
            handle_unknown_command(command, args)
        else:
            command_cls(command_registry=COMMANDS_NAMES_TO_CLASS).execute(args)


if __name__ == "__main__":
    main()
