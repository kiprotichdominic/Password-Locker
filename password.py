import random


class User:
    # saves user generated password
    user_pass = []

    def __init__(self, user_name, user_password):
        self.user_name = user_name
        self.user_password = user_password

    def save_password(self):
        User.user_pass.append(self)

    def delete_password(self):
        User.user_pass.remove(self)
        
    

class Credentials:
    pass
