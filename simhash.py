class SimHash:

    # 构造函数
    def __init__(self, tokens='', hash_bits=84):
        self.strHash = ''  # 记录数字指纹
        self.hash_bits = hash_bits  # 数字指纹位数
        self.hash = self.sim_hash(tokens)

    # toString函数
    def __str__(self):
        return str(self.hash)

    # 生成simHash值与strHash值
    def sim_hash(self, tokens):
        v = [0] * self.hash_bits
        for t in [self._string_hash(x) for x in tokens]:  # t为token的普通hash值
            for i in range(self.hash_bits):
                bitmask = 1 << i
                if t & bitmask:
                    v[i] += 1  # 查看当前bit位是否为1, 是的话将该位+1
                else:
                    v[i] -= 1  # 否则的话, 该位-1
        fingerprint = 0
        for i in range(self.hash_bits):
            if v[i] >= 0:
                self.strHash += '1'  # 若是整数则置1
                fingerprint += 1 << i
            else:
                self.strHash += '0'  # 否则置0
        return fingerprint  # 整个文档的fingerprint为最终各个位>=0的和

    # 针对source生成hash值   (一个可变长度版本的Python的内置散列)
    def _string_hash(self, source):
        if source == "":
            return 0
        else:
            x = ord(source[0]) << 7
            m = 1000003
            mask = 2 ** self.hash_bits - 1
            for c in source:
                x = ((x * m) ^ ord(c)) & mask
            x ^= len(source)
            if x == -1:
                x = -2
            return x

    # 求相似度
    def similarity(self, other):
        like = 0
        for i in range(len(self.strHash)):
            if int(self.strHash[i]) == int(other.strHash[i]):
                like += 1  # 通过数字指纹得到相似的段, 然后再计算相似度
        return float(like) / float(self.hash_bits)
