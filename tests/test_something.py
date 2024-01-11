import unittest


class TestSomething(unittest.TestCase):
    def test_case_1(self):
        # Test case 1
        self.assertEqual(2 + 2, 4)

    def test_case_2(self):
        # Test case 2
        self.assertNotEqual(3 * 5, 15)

    def test_case_3(self):
        # Test case 3
        self.assertTrue(True)

    def test_case_4(self):
        # Test case 4
        self.assertFalse(False)

    def test_case_5(self):
        # Test case 5
        self.assertIsNone(None)

    def test_case_6(self):
        # Test case 6
        self.assertIsNotNone("Hello")

if __name__ == '__main__':
    unittest.main()
