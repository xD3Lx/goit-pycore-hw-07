class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self.value
    
    @value.setter
    def value(self, val: str):
        if len(val.strip()) == 0:
            raise ValueError("Name cannot be empty")
        self.value = val


class Phone(Field):
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self.value
    
    @value.setter
    def value(self, val: str):
        if len(val) != 10 or not val.isdigit():
            raise ValueError("Phone number must contain only 10 digits")
        self.value = val