import unittest
import time
import random
from Common.Common_Log import MeiyinLog
logger = MeiyinLog().get_log()


class Meiyin_Port(unittest.TestCase):

    def setUp(self):
        logger.info("*************************用例{}开始执行***************************".format(self))
        self.headers = {"appId": "wxe36d354edaff0317",
           "deviceId": "android",
           "macId": "juLoEbCTWJwtB/qI1MRNW52fYaUb9Bb0K6WZFzy4FE7OlFRd5QCxT6uCXUVRyulMWUOrDgbVPsa2On0oRLtzN5k9GGAMVP+UKNyp26yZimPpvhcRA5BEQfbOI/9lVdByFEXBn5YRMt1nYdD9h4TgGNCW8zmjHY5bJggL8mf7uTo=",
           "h-nonce": "4a91903c-bbc6-4b9d-a976-8aabd0501c06",
           "h-system-code": "android",
           "versionName": "1.6.2.2",
           'random':str(random.randint(1000000000, 9000000000)),
           'timestamp':str(round(time.time() * 1000))
           }
        self.logger = MeiyinLog().get_log()



    def tearDown(self):
        self.logger.info("*************************用例{}执行结束***************************".format(self))

    @classmethod
    def setUpClass(cls):
        logger.info('************************测试类{}开始运行*************************'.format(cls))

    @classmethod
    def tearDownClass(cls):
        logger.info('************************测试类{}运行结束*************************'.format(cls))
