import random


class User:
    # saves user generated password
    user_pass = []

    def __init__(self, user_name, user_password):
        self.user_name = user_name
        self.user_password = user_password

    def save_users(self):
        User.user_pass.append(self)

    def delete_user(self):
        User.user_pass.remove(self)

    @classmethod
    def find_by_username(cls, username):
        for user in cls.user_pass:
            if user.user_name == username:
                return True

    @classmethod
    def display_user(cls):
        return cls.user_pass


class Credentials:
    pass
