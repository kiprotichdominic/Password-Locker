class User:
    user_list = []

    def __init__(self, name, user_password):
        self.user_name = name
        self.user_password = user_password

    def save_user(self):
        User.user_list.append(self)

    def delete_user(self):
        User.user_list.remove(self)

    @classmethod
    def find_by_username(cls, name):
        for user in cls.user_list:
            if user.user_name == name:
                return user

    @classmethod
    def user_exists(cls, name):
        for user in cls.user_list:
            if user.user_name == name:
                return True
            return False

    @classmethod
    def display_users(cls):
        return cls.user_list

    @classmethod
    def display_all_users(cls):
        return cls.user_list

    @classmethod
    def login_user(cls):
        return User.login_user()
