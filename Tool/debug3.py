import os,re
from Common.Common_Conf import path
from collections import Counter

def process():
    linelist = []
    errlist = []
    alllist = []
    try:
        subdir = os.listdir(path)
        for f in subdir: # 遍历文件夹下的文件
            text = open(path+f, 'r', encoding='utf-8')
            for lines in text.readlines():
                lines = lines.replace("\n", "").split(",")
                if 'ERROR' in str(lines):
                    if 'test_' in str(lines):
                        errlist.append(re.findall(r"] (.+?).py", str(lines))[0])
                if 'line:33' in str(lines):
                    linelist.append(lines)
                if '接口运行完毕' in str(lines):
                    alllist.append(lines)
        num = Counter(errlist)
        logger.info('报错个数:{},总接口数:{},运行次数:{}'.format(len(errlist), len(linelist), len(alllist)))
        #print(len(errlist), len(linelist), len(alllist), dict(num))
        return len(errlist), len(linelist), len(alllist), dict(num)
    except Exception as e:
        logger.error(e)
        pass


if __name__ == '__main__':
    process()