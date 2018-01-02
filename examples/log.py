# -*- coding: utf-8 -*-

from IOTSeedSDK.log import IOTSeedLogger
import time


if __name__ == "__main__":
    logger1 = IOTSeedLogger('demo test', '','CONSOLE')
    logger2 = IOTSeedLogger('logger2','','ROTATED','test.log')
    logger3 = IOTSeedLogger('logger3', '','DAILY', 'test.log')
    while True:
        logger1.write(u'测试日志1','Info', 'log')
        logger2.write(u'测试日志2', 'Info', 'log')
        logger3.write(u'测试日志3', 'Info', 'log')
        time.sleep(2)