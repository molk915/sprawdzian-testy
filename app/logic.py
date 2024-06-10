from datetime import datetime
from .models import User

class UserManager:
    def __init__(self):
        self.users = []
        self.next_id = 1

    def add_user(self, firstName, lastName, birthYear, group):
        if group not in ["user", "premium", "admin"]:
            raise ValueError("Invalid group")
        user = User(self.next_id, firstName, lastName, birthYear, group)
        self.users.append(user)
        self.next_id += 1
        return user

    def get_user(self, user_id):
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def get_all_users(self):
        return self.users

    def update_user(self, user_id, firstName=None, lastName=None, birthYear=None, group=None):
        user = self.get_user(user_id)
        if not user:
            return None
        
        if firstName:
            user.firstName = firstName
        if lastName:
            user.lastName = lastName
        if birthYear:
            user.birthYear = birthYear
        if group:
            if group not in ["user", "premium", "admin"]:
                raise ValueError("Invalid group")
            user.group = group
        
        return user

    def delete_user(self, user_id):
        user = self.get_user(user_id)
        if not user:
            return None
        self.users.remove(user)
        return user
