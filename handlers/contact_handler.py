from decorators.input_error import input_error
from model.address_book import AddressBook
from model.record import Record

def generate_contact_not_found_message(name):
    return f"Contact {name} does not exist."

@input_error
def add_contact(args, book: AddressBook):
    """
    Add a new contact or update an existing contact with a phone number.
    Args:
        args (list): A list containing at least a name and a phone number.
        book (AddressBook): The address book object where contacts are stored.
    Returns:
        str: A message indicating whether the contact was added or updated.
             Returns "Contact added." if a new contact was created,
             or "Contact updated." if an existing contact was modified.
    """
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def change_contact(args, book: AddressBook) -> str:
    """
    Add a phone number to an existing contact in the address book.
    Args:
        args (list): A list containing at least a name and a phone number.
        book (AddressBook): The address book instance containing contacts
    Returns:
        str: A message indicating the result of the operation:
            - "Phone number is already associated with this contact." if the phone 
              number already exists for the contact
            - f"Contact {name} does not exist." if the contact is not found in the 
              address book
            - "Contact updated." if the phone number was successfully added to the contact
    """ 
    name, phone, *_ = args
    record = book.find(name)
    if record is not None:
        phone_numbers = [phone.value for phone in record.phones]

        if phone in phone_numbers:
            return "Phone number is already associated with this contact."
        else:
            record.add_phone(phone)
            return "Contact updated."
    else:
        return generate_contact_not_found_message(name)

@input_error
def show_phone(args, book: AddressBook) -> str:
    """
    Retrieve and display phone number(s) for a contact.
    Args:
        args: A list of arguments where args[0] is the contact name.
        book: An AddressBook instance containing contact records.
    Returns:
        A string containing:
        - Comma-separated phone numbers if the contact exists and has phones
        - "No phone number found for this contact." if contact exists but has no phones
        - "Contact {name} does not exist." if the contact is not found
    """
    name = args[0]
    record = book.find(name)
    if record:
        if record.phones:
            return ", ".join(phone.value for phone in record.phones)
        else:
            return "No phone number found for this contact."
    else:
        return generate_contact_not_found_message(name)

@input_error
def all(args, book: AddressBook) -> str:
    """
    Display all contacts in the address book.

    Args:
        args: Command arguments (unused).
        book (AddressBook): The address book containing contacts.
    Returns:
        str: A formatted string of all contacts separated by newlines,
            or "No contacts found." if the address book is empty.
    """
    if (len(book) == 0):
        return "No contacts found."
    else:
        return "\n".join([str(record) for record in book.values()])
    
@input_error
def add_birthday(args, book: AddressBook) -> str:
    """
    Add a birthday to an existing contact in the address book.
    Args:
        args (list): A list containing the contact name and birthday.
        book (AddressBook): The address book object containing contacts.
    Returns:
        str: A success message if the birthday was added, or an error message
             if the contact was not found.
    """
    name, birthday, *_ = args
    record = book.find(name)
    if record is not None:
        record.add_birthday(birthday)
        return "Birthday added."
    else:
        return generate_contact_not_found_message(name)
    
@input_error
def show_birthday(args, book):
    """
    Retrieve and display the birthday information for a contact.
    Args:
        args (list): A list of arguments where the first element is the contact name.
        book (AddressBook): The address book object containing contact records.
    Returns:
        str: The birthday value if found, a message indicating no birthday information,
             or a contact not found message.
    """
    name, *_ = args
    record = book.find(name)
    if record is not None:
        if record.birthday:
            return record.birthday.value
        else:
            return f"No birthday information found for {name}."
    else:
        return generate_contact_not_found_message(name)

@input_error
def birthdays(args, book: AddressBook) -> str:
    """
    Retrieve upcoming birthdays from the address book.
    Args:
        args: Command arguments (unused).
        book (AddressBook): The address book object containing contacts.
    Returns:
        str: A string representation of upcoming birthdays from the address book.
    """
    return str(book.get_upcoming_birthdays())

@input_error
def close(args, contacts):
    return "Good bye!"

@input_error
def hello(args, contacts):
    return "How can I help you?"