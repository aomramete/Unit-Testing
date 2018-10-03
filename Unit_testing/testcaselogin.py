import unittest
import login

class TestCode(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(login.login('aom','123456'),1)
    def test_case2(self):
        self.assertEqual(login.login('aom','12346'),0)
    def test_case3(self):
        self.assertEqual(login.login('aommmmm','123456'),0)
    def test_case4(self):
        self.assertEqual(login.login('neenongaom','12346'),0)

if __name__ == '__main__':
    unittest.main()
