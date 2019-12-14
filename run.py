from password import User


def create_user(user_name, user_password):
    new_user = User(user_name, user_password)
    return new_user


def save_user(user):
    user.save_user()


def delete_user(user):
    user.delete_user()


def find_user(username):
    return User.find_by_username(username)


def diplay_user():
    return User.display_user()


def main():
    user_name = input()
    
    print("Hello {User_name}. Welcome to password locker. Create strong passwords.")
