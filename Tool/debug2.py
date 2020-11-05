import time
from Common.Common_Excel import get_nrows,get_xls
from Common.Common_Conf import expath
from Common.Common_Log import MeiyinLog

logger = MeiyinLog().get_log()

xlsc,shtc = get_xls()
number = get_nrows()
path = "H:\\美印\\tt_log\\"
name =  time.strftime("%Y_%m_%d_")+'test'+'.log'
file = path+name
# 筛选列表
portlist = ['usercenter/sign', 'editUserInfo','getMessageGroup','productSearch',
            'getProductInfo','checkCodeIsOk','getMineWallet','addAlbum','delAlbumBatch','editAddressNew',
            ]

def add_rtime():
    with open(file, 'r', encoding='utf-8') as f:
        for lines in f.readlines():
            lines = lines.replace("\n", "").split(",")
            if 'loginByPhone' in str(lines):
                a = str(lines)[3:22] + ',' + str(lines)[26:29]
                shtc.write(number, 0, a)
                shtc.write(number, 1, lines[2])
                print(lines[2])
                xlsc.save(r'%s' % expath)

            for i in portlist:
                if i in str(lines):
                    b = portlist.index(i)+2
                    shtc.write(number, b, lines[2])
                    xlsc.save(r'%s' % expath)
        logger.info('响应时间EXCEL保存完毕')

add_rtime()