from model.fields import Name, Phone

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        """
        Add a phone number to the contact's phone list.
        Args:
            phone_number (str): The phone number to add to the contact.
        Returns:
            None
        """
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number):
        """
        Remove a phone number from the contact's phone list.
        Args:
            phone_number (str): The phone number to remove from the contact's phones.
        Returns:
            None
        """
        self.phones = list(filter(lambda p: p.value != phone_number, self.phones))
    
    def edit_phone(self, old_phone, new_phone):
        """
        Edit a phone number in the contact record.
        
        Replaces an existing phone number with a new one. Searches through all phones
        in the record and replaces the phone with a value matching old_phone with a
        new Phone object containing new_phone.
        
        Args:
            old_phone (str): The phone number value to search for and replace.
            new_phone (str): The new phone number value to set.
        
        Returns:
            None
        """
        self.phones = [(Phone(new_phone) if p.value == old_phone else p) for p in self.phones]

    def find_phone(self, phone_number):
        """
        Find a phone record by its phone number value.
        Args:
            phone_number (str): The phone number value to search for.
        Returns:
            Phone: The phone object if found, None otherwise.
        """

        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
