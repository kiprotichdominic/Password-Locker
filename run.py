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
