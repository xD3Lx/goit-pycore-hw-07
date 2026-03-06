from decorators.input_error import input_error

@input_error
def add_contact(args, contacts):
    """
    Add a new contact to the contacts dictionary.
    Args:
        args (tuple): A tuple containing two elements:
            - name (str): The name of the contact to add.
            - phone (str): The phone number of the contact.
        contacts (dict): A dictionary storing contacts.
    Returns:
        str: A message indicating whether the contact was successfully added or if it already exists.
            - "Contact added." if the contact was successfully added.
            - "Contact {name} already exists." if a contact with the same name already exists.
    """

    name, phone = args
    if name in contacts:
        return f"Contact {name} already exists."
    else:
        contacts[name] = phone
        return "Contact added."

@input_error
def change_contact(args, contacts):
    """
    Update an existing contact's phone number.
    Args:
        args (tuple): A tuple containing two elements:
            - name (str): The name of the contact to update.
            - phone (str): The new phone number for the contact.
        contacts (dict): A dictionary storing contacts.
    Returns:
        str: A message indicating whether the contact was successfully updated
             or if the contact does not exist.
    """

    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:        
        return f"Contact {name} does not exist."

@input_error
def show_phone(args, contacts):
    """
    Retrieve and display the phone number for a given contact.
    Args:
        args (list): A list containing the contact name as the first element.
        contacts (dict): A dictionary storing contacts.
    Returns:
        str: The phone number associated with the contact name, or an error message 
             if the contact does not exist.
    """

    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return f"Contact {name} does not exist."

@input_error
def all(args, contacts):
    """
    Display all contacts from the contacts dictionary.
    Args:
        args (list): A list of arguments (should be empty for this command).
        contacts (dict): A dictionary storing contacts.
    Returns:
        str: A string containing all contacts in the format "name: phone" separated by newlines,
             or "No contacts found." if the contacts dictionary is empty.
    """

    output = []

    if (len(contacts) == 0):
        return "No contacts found."
    else:
        for name, phone in contacts.items():
            output.append(f"{name}: {phone}")
        return "\n".join(output)

@input_error
def close(args, contacts):
    return "Good bye!"

@input_error
def hello(args, contacts):
    return "How can I help you?"