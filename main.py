from commands import COMMANDS_NAMES_TO_CLASS


def get_command_and_args_from_user_input(user_input: str) -> tuple[str, list[str]]:
    splitted_input = user_input.split(" ")
    command = splitted_input[0]
    args = splitted_input[1:] if len(splitted_input) > 1 else []
    return command, args


def main():
    while True:
        user_input = input("$ ")
        command, args = get_command_and_args_from_user_input(user_input)
        command_cls = COMMANDS_NAMES_TO_CLASS.get(command)
        if not command_cls:
            print(f"{user_input}: command not found")
        else:
            command_cls(command_registry=COMMANDS_NAMES_TO_CLASS).execute(args)


if __name__ == "__main__":
    main()
