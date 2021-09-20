import unittest
from main import main_test

path1 = 'orig.txt'
path2 = 'orig_0.8_add.txt'
path3 = 'orig_0.8_del.txt'
path4 = 'orig_0.8_dis_1.txt'
path5 = 'orig_0.8_dis_10.txt'
path6 = 'orig_0.8_dis_15.txt'
pathError = 'a.txt'


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(main_test(path1, path2), 0.85)

    def test_2(self):
        self.assertEqual(main_test(path1, path3), 0.86)

    def test_3(self):
        self.assertEqual(main_test(path1, path4), 0.85)

    def test_4(self):
        self.assertEqual(main_test(path1, path5), 0.86)

    def test_5(self):
        self.assertEqual(main_test(path1, path6), 0.86)

    def test_6(self):
        self.assertEqual(main_test(path1, pathError), 0.99)

    def test_7(self):
        self.assertEqual(main_test(pathError, path1), 0.99)


if __name__ == '__main__':
    unittest.main()
