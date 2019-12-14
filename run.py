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


def display_user():
    return User.display_user()


def main():
    user_name = input()

    print(
        "Hello {User_name}. Welcome to password locker. Create strong passwords.")
    print("\n")

    while True:
        print(
            """
Use these short codes:
cu - create user
du - display user
fu - find user
del - delete user
esc - exit the program
            """

        )
        short_code = input().lower()

        if short_code == "cu":
            print("Create an new user")
            print("-" * 10)
