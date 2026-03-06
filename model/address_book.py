from collections import UserDict
from datetime import datetime, timedelta
from typing import Dict, List

from model.record import Record

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
            raise KeyError(f"Contact with name '{record.name.value}' already exists.")
        self.data[record.name.value] = record

    def find(self, name) -> Record:
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
            raise KeyError(f"Contact with name '{name}' not found.")
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
            raise KeyError(f"Contact with name '{name}' not found.")
        del self.data[name]

    def get_upcoming_birthdays(self) -> List[Dict[str, str]]:
        """
        Identify upcoming birthdays within the next 7 days and schedule congratulation dates.
        This function processes a list of users, finds those with birthdays occurring within
        the next 7 days, and adjusts the congratulation date to the following Monday if the
        birthday falls on a weekend.
        Args:
            self: The instance of the AddressBook class containing user records with birthday information.
        Returns:
            list: A list of dictionaries containing upcoming birthdays with keys:
                - "name" (str): The user's name
                - "congratulation_date" (str): The date to send congratulations in format "%Y.%m.%d"
                    (moved to Monday if the birthday falls on weekend)
        Example:
            >>> users = [
            ...     {"name": "John Doe", "birthday": "1985.03.05"},
            ...     {"name": "Jane Smith", "birthday": "1990.03.07"},
            ...     {"name": "Michael Kim", "birthday": "1990.02.01"}
            ... ]
            >>> get_upcoming_birthdays(users)
            [{'name': 'John Doe', 'congratulation_date': '2026.03.05'}, {'name': 'Jane Smith', 'congratulation_date': '2026.03.09'}]
        """

        today_date = datetime.today().date()
        upcoming_birthdays = []

        for _, user in self.data.items():
            if user.birthday is None:
                continue

            #Parse the birthday string into a datetime object
            birthday = datetime.strptime(user.birthday.value, "%d.%m.%Y").date()
            #Replace the year of the birthday with the current year
            birthday_this_year = birthday.replace(year=today_date.year)

            #If the birthday has already passed this year, move it to the next year
            if birthday_this_year < today_date:
                birthday_this_year = birthday_this_year.replace(year=today_date.year + 1)

            #Calculate the number of days until the birthday
            days_to_birthday = (birthday_this_year - today_date).days

            #Check if the birthday is within the next 7 days
            if 0 <= days_to_birthday <= 7:
                congratulation_date = birthday_this_year

                # if the burthday falls on a weekend (Saturday=5, Sunday=6)
                if congratulation_date.weekday() >= 5:  
                    #Move to the next Monday
                    congratulation_date += timedelta(days=(7 - congratulation_date.weekday())) 

                upcoming_birthdays.append({
                    "name": user.name.value,
                    "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
                })

        return upcoming_birthdays