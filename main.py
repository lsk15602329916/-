import re
import os
from simhash import SimHash


def get_file_contents(path):
    string = ''
    f = open(path, 'r', encoding='UTF-8')
    line = f.readline()
    while line:
        string = string + line
        line = f.readline()
    f.close()
    return string


if __name__ == '__main__':

    dir_path = os.path.dirname(os.path.abspath(__file__)) + '\\content\\'

    path1 = input("输入论文原文的文件的相对路径：")
    PATH1 = dir_path + path1
    if not os.path.exists(PATH1) :
        print("论文原文文件不存在！")
        exit()

    path2 = input("输入抄袭版论文的文件的相对路径：")
    PATH2 = dir_path + path2
    if not os.path.exists(PATH2):
        print("抄袭版论文文件不存在！")
        exit()

    str1 = get_file_contents(PATH1)
    str2 = get_file_contents(PATH2)

    save_path = dir_path + "\\result.txt"
    try:

        hash1 = SimHash(re.split(r'[，。！、：“”]', str1.replace('\n', '')))  # 分段后计算每段的哈希值与数字指纹
        hash2 = SimHash(re.split(r'[，。！、：“”]', str2.replace('\n', '')))
        result = hash1.similarity(hash2)

        with open(save_path, 'a', -1, 'utf-8') as f:
            f.write(path1 + ' 与 ' + path2)
            f.write(' 的相似度为：' + str(round(result, 2)) + '\n')  # 通过数字指纹算出相似值
            print(path1 + ' 与 ' + path2 +' 的相似度为：' + str(round(result, 2)) + '\n')
            
    except IOError:
        print('错误: 没有找到文件或读取文件失败!')
    except IndexError:
        print('错误: 参数缺失, 需要依次输入两个读入文件以及一个输出结果的文件!')
