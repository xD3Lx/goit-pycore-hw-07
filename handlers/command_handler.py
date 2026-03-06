from handlers.contact_handler import (
    add_birthday,
    add_contact,
    birthdays, 
    change_contact,
    show_birthday, 
    show_phone, 
    all, 
    close,
    hello
)


COMMANDS_TO_HANDLERS = {
    "exit": close,
    "close": close,
    "hello": hello,
    "add": add_contact,
    "change": change_contact,
    "phone": show_phone,
    "all": all,
    "add-birthday": add_birthday,
    "show-birthday": show_birthday,
    "birthdays": birthdays,
}


def handle_command(command, args, contacts):
    """
    Route and execute commands based on user input.
    Args:
        command (str): The command name to be executed.
        args (list): Arguments to pass to the command handler.
        contacts (dict): The contacts dictionary to operate on.
    Returns:
        str: The result of the command execution, or an error message if the command is invalid.
    Note:
        Supported commands: exit, close, hello, add, change, phone, all
    """

    handler = COMMANDS_TO_HANDLERS.get(command)
    if handler:
        return handler(args, contacts)
    else:
        return "Invalid command."