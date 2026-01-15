import unittest
from vault_security import check_password

class TestVaultSecurity(unittest.TestCase):

    def test_password_length(self):
        self.assertFalse(check_password("abc"))

    def test_password_numbers(self):
        self.assertFalse(check_password("abcdefgh"))  # sense números
        self.assertTrue(check_password("Abcd1234"))   # amb números i majúscula

    def test_password_uppercase(self):
        self.assertFalse(check_password("abcd1234"))  # sense majúscules
        self.assertTrue(check_password("Abcd1234"))   # amb majúscules

    def test_password_no_admin(self):
        self.assertFalse(check_password("admin1234"))  # conté "admin"
        self.assertTrue(check_password("Secure123"))   # correcte

if __name__ == "__main__":
    unittest.main()
