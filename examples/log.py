# -*- coding: utf-8 -*-

from IOTSeedSDK.log import Logger
import time


if __name__ == "__main__":
    logger1 = Logger('demo test', 'CONSOLE')
    logger2 = Logger('logger2','ROTATED','test.log')
    while True:
        logger1.write(u'测试日志1','Info')
        logger2.write(u'测试日志2', 'Info')
        time.sleep(2)
