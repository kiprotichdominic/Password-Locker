from password import User
import random
import string
from getpass import getpass


def create_user(name, user_password):
    """

    Parameters
    ----------
    name
    user_password

    Returns
    -------

    """
    new_user = User(name, user_password)
    return new_user


def login_user(name, user_password):
    """

    Parameters
    ----------
    name
    user_password

    Returns
    -------

    """
    return User.login_user()


def generate_password(user):
    """

    function to generate random password for user
    ----------
    user

    Returns
    -------

    """
    return User.generate_random_password()


def save_user(user):
    """

    Function to save user
    ----------
    user
    """
    user.save_user()


def delete_user(user):
    """

    Function to delete user
    ----------
    user
    """
    user.delete_user()


def find_user(name):
    """

    Function to find user
    ----------
    name

    Returns
    -------

    """
    return User.find_by_username(name)


def check_existing_users(name):
    """

    Function to check existing users
    ----------
    name

    Returns
    -------
    user

    """
    return User.find_by_username(name)


def display_users():
    """
    Function to display users

    Returns
    -------

    """
    return User.display_all_users()


def main():
    """

    Returns
    -------

    """
    user_name = input("Enter your name > ")

    print(f"Hello {user_name}, welcome to password locker")
    print("\n")
    ask = input(f"Hello {user_name}. Do you have an Account? YES/N0 > ")

    if ask == "no":
        print("Signup with password locker to have access")
        user_name = input("Enter your User name > ")
        create = input(
            f"Hello {user_name}. Do you want a generated password? YES/N0 > ")
        if create == "no":
            user_password = input("Enter your password > ")
        elif create == "yes":
            def random_password(string_length):
                """

                Parameters
                ----------
                string_length

                Returns
                -------

                """
                letters = string.ascii_letters
                return "".join(random.choice(letters) for i in range(string_length))
            print(
                f"Your random password is: ", random_password(8))
            print("You are now logged in: ")
        while True:
            print("""
            USE THE SHORT CODES
    1. cu - to create a new user
    2. du - to display users
    3. fu - to find users
    4. gp - to generate a random password
    4. esc - to quit
            """)
            short_code = input("Use short-codes to navigate > ").lower()

            if short_code == "cu":
                print("Create Your Password Locker Account")
                print("-" * 10)

                print("First name ....")
                user_name = input("> ")

                print("Enter Password")
                user_password = getpass("> ")

                save_user(create_user(user_name, user_password))

                print("\n")
                print(f"New User {user_name} {user_password} has been created")
                print("\n")

            elif short_code == "gp":
                print(
                    "Please enter the social media you want to generate password for > ")
                social_media = input("Enter account type > ")

                def random_password(string_length):
                    """

                    Parameters
                    ----------
                    string_length

                    Returns
                    -------

                    """
                    letters = string.ascii_letters
                    return "".join(random.choice(letters) for i in range(string_length))
                print(
                    f"Your random password for {social_media} is: ", random_password(8))

            elif short_code == "du":

                if display_users():
                    print("Here is a list of all your Username's and passwords")
                    print("\n")
                    for user in display_users():
                        print(f"{user.user_name} {user.user_password}")
                        print("\n")
                    else:
                        print("\n")
                        print(
                            "You don't have any saved passwords yet. Try saving one")
                        print("\n")

            elif short_code == "fu":
                print("Enter the username of the user you would like to search for.")

                search_name = input()
                if check_existing_users(search_name):
                    search_name = find_user(search_name)
                    print(f"{find_user.user_name} {find_user.user_password} ")
                    print("-" * 20)

                    print(f"User Name: {find_user.user_name}")
                    print(f"User password: {find_user.user_password}")

                else:
                    print("That contact does not exist")

            elif short_code == "esc":
                print("Logged out")
                break
            else:
                print("I really didn't get that. Please use the short codes")


if __name__ == "__main__":
    main()
