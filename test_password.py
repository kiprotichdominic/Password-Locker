import unittest
from password import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("Kiprotich", "12345678")




    def tearDown(self):
        User.user_list = []


if __name__ == "__main__":
    unittest.main()