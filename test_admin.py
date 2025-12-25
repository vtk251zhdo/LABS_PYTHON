import unittest
from admin import Admin, Privileges


class TestAdmin(unittest.TestCase):

    def setUp(self):
        self.admin = Admin(
            "Admin",
            "User",
            "admin@example.com",
            "AdminNick",
            True
        )

    def test_admin_basic_info(self):
        self.assertEqual(self.admin.first_name, "Admin")
        self.assertEqual(self.admin.last_name, "User")
        self.assertEqual(self.admin.email, "admin@example.com")
        self.assertEqual(self.admin.nickname, "AdminNick")

    def test_privileges_object_exists(self):
        self.assertIsInstance(self.admin.priv, Privileges)

    def test_privileges_list_exists(self):
        self.assertIsInstance(self.admin.priv.privileges, list)
        self.assertGreater(len(self.admin.priv.privileges), 0)


if __name__ == "__main__":
    unittest.main()

# python -m unittest test_admin.py