import unittest
from password import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("Kiprotich", "12345678")

    def test_init(self):
        self.assertEqual(self.new_user.user_name, "Kiprotich")
        self.assertEqual(self.new_user.user_password, "12345678")
        
    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)
        
    def test_save_multiple_users(self):
        self.new_user.save_user()
        test_user = User("facebook", "1234")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)


    def tearDown(self):
        User.user_list = []


if __name__ == "__main__":
    unittest.main()