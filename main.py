import re
import os
from simhash import SimHash
from fileUtils import get_file_contents


def main_test(p1, p2):
    dir_path = os.path.dirname(os.path.abspath(__file__)) + '\\content\\'

    PATH1 = dir_path + p1
    if not os.path.exists(PATH1):
        print("论文原文文件不存在！")
        exit()

    PATH2 = dir_path + p2
    if not os.path.exists(PATH2):
        print("抄袭版论文文件不存在！")
        exit()
    str1 = get_file_contents(PATH1)
    str2 = get_file_contents(PATH2)

    save_path = dir_path + "\\result.txt"
    hash1 = SimHash(re.split(r'[，。！、：“”]', str1.replace('\n', '')))  # 分段后计算每段的哈希值与数字指纹
    hash2 = SimHash(re.split(r'[，。！、：“”]', str2.replace('\n', '')))
    result = round(hash1.similarity(hash2), 2)

    with open(save_path, 'a', -1, 'utf-8') as f:
        f.write(p1 + ' 与 ' + p2)
        f.write(' 的相似度为：' + str(result) + '\n')  # 通过数字指纹算出相似值
        print(p1 + ' 与 ' + p2 + ' 的相似度为：' + str(result) + '\n')
        f.close()

    return result


if __name__ == '__main__':
    path1 = input("输入论文原文的文件的相对路径：")
    path2 = input("输入抄袭版论文的文件的相对路径：")
    main_test(path1, path2)
