from password import User


def create_user(user_name, user_password):
    new_user = User(user_name, user_password)
    return new_user


def save_user(user):
    user.save_user()
