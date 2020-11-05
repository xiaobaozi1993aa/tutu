import threading
import time
import unittest


def suite1():
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromName('Test_Case.test_login'))                          #登录
    runner = unittest.TextTestRunner()
    threadLock.acquire()
    runner.run(suite)
    threadLock.release()

def suite2():
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromName('Test_Case.Person.test_sign'))                    #签到
    runner = unittest.TextTestRunner()
    runner.run(suite)

def suite3():
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromName('Test_Case.Person.test_person'))                  # 更改姓名
    runner = unittest.TextTestRunner()
    runner.run(suite)


def suite4():
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromName('Test_Case.Person.test_getmessage'))                  # 更改姓名
    runner = unittest.TextTestRunner()
    runner.run(suite)

threadLock = threading.Lock()

if __name__ == '__main__':
    start = time.clock()

    threads = []

    t1 = threading.Thread(target=suite1)
    t2 = threading.Thread(target=suite2)
    t3 = threading.Thread(target=suite3)
    t4 = threading.Thread(target=suite4)

    threads.append(t1)
    threads.append(t2)
    threads.append(t3)
    threads.append(t4)

    for x in threads:
        x.start()
        x.join()
    print(time.clock() - start)
