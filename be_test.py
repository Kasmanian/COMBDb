import shutil
import unittest

from db import Database

class TestDatabase(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.db = Database()

    def test_connect_fail(self):
        is_connected = self.db.connect('')
        self.assertEqual(is_connected, False, 'Connection should fail')

    # def test_connect_pass(self):
    #     pass

if __name__ == '__main__':
    unittest.main()
