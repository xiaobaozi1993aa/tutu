import time
from Common.Common_Excel import get_nrows,get_xls
from Common.Common_Log import MeiyinLog
from collections import Counter
import re
from Common.Common_Conf import expath


logger = MeiyinLog().get_log()


path = "H:\\美印\\tt_log\\"
name =  time.strftime("%Y_%m_%d_")+'test'+'.log'
file = path+name
# 筛选列表
def add_errnum():
    xlsc, shtc = get_xls(1)
    number = get_nrows(1)
    linelist = []
    errlist = []
    alllist = []
    try:
        with open(file, 'r',encoding='utf-8') as f:
            for lines in f.readlines():
                lines = lines.replace("\n", "").split(",")
                if 'ERROR' in str(lines):
                    if 'test_' in str(lines):
                        print(str(lines))
                        b = (re.findall(r"] (.+?).py", str(lines))[0])
                        shtc.write(number, 3, b)

                if 'line:33' in str(lines):
                    linelist.append(lines)
                    shtc.write(number, 1, len(linelist))

                if '接口运行完毕' in str(lines):
                    alllist.append(lines)
                    shtc.write(number, 0, len(alllist))
            xlsc.save(r'%s' % expath)
            num = Counter(errlist)
            #logger.info('报错个数:{},总接口数:{},运行次数:{}'.format(len(errlist),len(linelist),len(alllist)))
            return len(errlist),len(linelist),len(alllist),dict(num)
    except Exception as e:
            logger.error(e)

#总运行数	总接口数	日期	报错接口	次数	超时接口	次数

if __name__ == '__main__':
    add_errnum()