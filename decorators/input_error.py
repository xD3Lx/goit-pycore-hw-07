def input_error(func):
    """
    A decorator that handles common errors in command processing functions.
    This decorator wraps functions to catch and handle specific exceptions that may
    occur during execution, returning user-friendly error messages instead of raising
    exceptions.
    Catches:
        KeyError: Returns "Contact does not exist." when a contact key is not found.
        ValueError: Returns "Enter the correct number of arguments for the command." when the required number of arguments is incorrect.
        IndexError: Returns "Enter the correct number of arguments for the command." when required arguments are missing.
        Exception: Catches any other unexpected exceptions and returns a generic error message.
    Returns:
        function: A wrapper function that executes the decorated function with error handling.
    """

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as e:
            return f"Error: {str(e)}"
        except ValueError as e:
            if "not enough values to unpack" in str(e):
                return "Enter the correct number of arguments for the command."
            else:
                return f"Error: {str(e)}"
        except IndexError:
            return "Enter the correct number of arguments for the command."
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"
    return inner