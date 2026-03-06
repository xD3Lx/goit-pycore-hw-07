from handlers.command_handler import handle_command
from model.address_book import AddressBook

def parse_input(user_input):
    """
    Parse user input into a command and its arguments.
    Args:
        user_input (str): The raw user input string to be parsed.
    Returns:
        tuple: A tuple containing the command (str) as the first element,
               followed by any number of arguments (str) as remaining elements.
    """

    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    book = AddressBook()

    print("Welcome to the assistant bot!")
    while True:
        # Get user input and parse it into a command and arguments
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        print(handle_command(command, args, book))

        # Check if the command is "close" or "exit" to terminate the chat
        if command in ["close", "exit"]:
            break

if __name__ == "__main__":
    main()