import re
from simhash import SimHash
import os
import cProfile

if __name__ == '__main__':

    # 获取当前目录绝对路径
    dir_path = os.path.dirname(os.path.abspath(__file__))

    regular = r'[，。！、：“”]'

    with open(dir_path + '\\content\\orig.txt', 'r', -1, 'utf-8') as f:
        s = f.read()

    hash1 = SimHash(re.split(regular, s.replace('\n', '')))

    with open(dir_path + '\\content\\orig_0.8_add.txt', 'r', -1, 'utf-8') as f:
        s = f.read()

    hash2 = SimHash(re.split(regular, s.replace('\n', '')))

    with open(dir_path + '\\content\\orig_0.8_del.txt', 'r', -1, 'utf-8') as f:
        s = f.read()

    hash3 = SimHash(re.split(regular, s.replace('\n', '')))

    with open(dir_path + '\\content\\orig_0.8_dis_1.txt', 'r', -1, 'utf-8') as f:
        s = f.read()

    hash4 = SimHash(re.split(regular, s.replace('\n', '')))

    with open(dir_path + '\\content\\orig_0.8_dis_10.txt', 'r', -1, 'utf-8') as f:
        s = f.read()

    hash5 = SimHash(re.split(regular, s.replace('\n', '')))

    with open(dir_path + '\\content\\orig_0.8_dis_15.txt', 'r', -1, 'utf-8') as f:
        s = f.read()

    hash6 = SimHash(re.split(regular, s.replace('\n', '')))

    with open(dir_path + '\\content\\other.txt', 'r', -1, 'utf-8') as f:
        s = f.read()

    hash7 = SimHash(re.split(regular, s.replace('\n', '')))

    print("orig.txt 与 orig_0.8_add.txt相似率为:\t\t", round(hash1.similarity(hash2), 2))
    print("orig.txt 与 orig_0.8_del.txt相似率为:\t\t", round(hash1.similarity(hash3), 2))
    print("orig.txt 与 orig_0.8_dis_1.txt相似率为:\t\t", round(hash1.similarity(hash4), 2))
    print("orig.txt 与 orig_0.8_dis_10.txt相似率为:\t\t", round(hash1.similarity(hash5), 2))
    print("orig.txt 与 orig_0.8_dis_15.txt相似率为:\t\t", round(hash1.similarity(hash6), 2))
    print("orig.txt 与 other.txt非抄袭文章的相似率为:\t", round(hash1.similarity(hash7), 2))
