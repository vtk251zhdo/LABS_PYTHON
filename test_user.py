import unittest
from user import User

class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User("Danyil", "Zhukovskyi", "zhukovskyi@example.com", "Eloquencert",
            True
        )
    
    def test_user_attributes(self):
        self.assertEqual(self.user.first_name, "Danyil")
        self.assertEqual(self.user.last_name, "Zhukovskyi")
        self.assertEqual(self.user.email, "zhukovskyi@example.com")
        self.assertEqual(self.user.nickname, "Eloquencert")
        self.assertEqual(self.user.login_attempts, 0)

    def test_increment_login_attempts(self):
        self.user.increment_login_attempts()
        self.assertEqual(self.user.login_attempts, 1)
        self.user.increment_login_attempts()
        self.assertEqual(self.user.login_attempts, 2)
    
    def test_reset_login_attempts(self):
        self.user.increment_login_attempts()
        self.user.increment_login_attempts()
        self.user.reset_login_attempts()
        self.assertEqual(self.user.login_attempts, 0)

if __name__ == '__main__':
    unittest.main()

# python -m unittest test_user.py