from collections import UserDict

class AddressBook(UserDict):
    def add_record(self, record):
        """
        Add a new record to the address book.
        
        Args:
            record: A Record object containing contact information
        
        Raises:
            KeyError: If a record with the same name already exists in the address book.
        
        Returns:
            None
        """
        if record.name.value in self.data:
            raise KeyError(f"Record with name '{record.name.value}' already exists.")
        self.data[record.name.value] = record

    def find(self, name):
        """
        Find a record in the address book by name.

        Args:
            name (str): The name of the record to find.

        Returns:
            Record: The record object associated with the given name.

        Raises:
            KeyError: If a record with the specified name is not found in the address book.
        """
        record = self.data.get(name, None)
        if record is None:
            raise KeyError(f"Record with name '{name}' not found.")
        return record


    def delete(self, name):
        """
        Delete a record from the address book by name.
        Args:
            name (str): The name of the record to delete.
        Raises:
            KeyError: If no record with the given name exists in the address book.
        """
        
        if name not in self.data:
            raise KeyError(f"Record with name '{name}' not found.")
        del self.data[name]