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


if __name__ == '__main__':
    unittest.main()
    #
    # try:
    #     # 获取当前目录绝对路径
    #     dir_path = os.path.dirname(os.path.abspath(__file__))
    #
    #     regular = r'[，。！、：“”]'
    #
    #     with open(dir_path + '\\content\\orig.txt', 'r', -1, 'utf-8') as f:
    #         s = f.read()
    #
    #     hash1 = SimHash(re.split(regular, s.replace('\n', '')))
    #
    #     with open(dir_path + '\\content\\orig_0.8_add.txt', 'r', -1, 'utf-8') as f:
    #         s = f.read()
    #
    #     hash2 = SimHash(re.split(regular, s.replace('\n', '')))
    #     print("orig.txt 与 orig_0.8_add.txt相似率为:\t\t", round(hash1.similarity(hash2), 2))
    #
    #     with open(dir_path + '\\content\\orig_0.8_del.txt', 'r', -1, 'utf-8') as f:
    #         s = f.read()
    #
    #     hash3 = SimHash(re.split(regular, s.replace('\n', '')))
    #     print("orig.txt 与 orig_0.8_del.txt相似率为:\t\t", round(hash1.similarity(hash3), 2))
    #
    #     with open(dir_path + '\\content\\orig_0.8_dis_1.txt', 'r', -1, 'utf-8') as f:
    #         s = f.read()
    #
    #     hash4 = SimHash(re.split(regular, s.replace('\n', '')))
    #     print("orig.txt 与 orig_0.8_dis_1.txt相似率为:\t\t", round(hash1.similarity(hash4), 2))
    #
    #     with open(dir_path + '\\content\\orig_0.8_dis_10.txt', 'r', -1, 'utf-8') as f:
    #         s = f.read()
    #
    #     hash5 = SimHash(re.split(regular, s.replace('\n', '')))
    #     print("orig.txt 与 orig_0.8_dis_10.txt相似率为:\t", round(hash1.similarity(hash5), 2))
    #
    #     with open(dir_path + '\\content\\orig_0.8_dis_15.txt', 'r', -1, 'utf-8') as f:
    #         s = f.read()
    #
    #     hash6 = SimHash(re.split(regular, s.replace('\n', '')))
    #     print("orig.txt 与 orig_0.8_dis_15.txt相似率为:\t", round(hash1.similarity(hash6), 2))
    #
    #     with open(dir_path + '\\content\\wewe.txt', 'r', -1, 'utf-8') as f:
    #         s = f.read()
    #
    #     hash8 = SimHash(re.split(regular, s.replace('\n', '')))
    #     print("orig.txt 与 other.txt非抄袭文章的相似率为:\t", round(hash1.similarity(hash8), 2))
    #
    # except IOError:
    #     print('错误: 没有找到文件或读取文件失败!')
