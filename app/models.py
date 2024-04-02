from datetime import datetime

class User:
    def __init__(self, id, firstName, lastName, birthYear, group):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.birthYear = birthYear
        self.group = group
        
    def to_dict(self):
        return {
            "id": self.id,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "age": datetime.now().year - self.birthYear,
            "group": self.group
        }
