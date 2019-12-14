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
        
    def test_delete_user(self):
        self.new_user.save_user()
        test_user = User("Kiprotich", "12345678")
        test_user.save_user()
        
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 1)
        
    def test_find_user_by_user_name(self):
        self.new_user.save_user()
        test_user = User("kiprotich", "12345678")
        test_user.save_user()
        
        found_user = User.find_by_username("kiprotich")
        self.assertEqual(found_user.user_name, test_user.user_name)
        
        
    def test_user_exists(self):
        self.new_user.save_user()
        test_user = User("Kiprotich", "12345678")
        test_user.save_user()
        user_exists = User.contact_exists("Kiprotich")
        self.assertTrue(user_exists)
        
    def test_display_user(self):
        self.assertEqual(user.display_users(), User.user_list)


    def tearDown(self):
        User.user_list = []


if __name__ == "__main__":
    unittest.main()