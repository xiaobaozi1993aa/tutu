import time
from Common.Common_Excel import get_nrows,get_xls
from Common.Common_Log import MeiyinLog
import re
from collections import Counter
logger = MeiyinLog().get_log()

xlsc,shtc = get_xls()
number = get_nrows()
path = "H:\\美印\\tt_log\\"
name =  time.strftime("%Y_%m_%d_")+'test'+'.log'
file = path+name
def add_errnum():
    linelist = []
    errlist = []
    alllist = []
    try:
        with open(file, 'r',encoding='utf-8') as f:
            for lines in f.readlines():
                lines = lines.replace("\n", "").split(",")
                if 'ERROR' in str(lines):
                    if 'test_' in str(lines):
                        errlist.append(re.findall(r"] (.+?).py", str(lines))[0])
                if 'line:33' in str(lines):
                    linelist.append(lines)
                if '接口运行完毕' in str(lines):
                    alllist.append(lines)
            num = Counter(errlist)
            logger.info('报错个数:{},总接口数:{},运行次数:{}'.format(len(errlist),len(linelist),len(alllist)))
            return len(errlist),len(linelist),len(alllist),dict(num)
    except Exception as e:
            logger.error(e)

errnum,portnum,runnum,errnum_list = add_errnum()

port_name = list(errnum_list.keys())
port_num = list(errnum_list.values())
