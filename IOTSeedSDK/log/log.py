# -*- coding: utf-8 -*-


import logging
import sys
import logging.handlers

_IOTSEED_LOG_TYPE_ = ['CONSOLE','DAILY','ROTATED']

_IOTSEED_LOG_LEVEL_ = ['Info','Warn','Err','Critical']


class Logger(object):
    def __init__(self, name, type="CONSOLE", path=None):
        self.__name = name
        self.__type = type
        self._logger = self._create_logger(path)

    def _create_logger(self, path=None):
        handler = None
        _logger = logging.getLogger(self.__name)
        _logger.setLevel(logging.INFO)  # 所有日志都会被记录
        if self.__type not in _IOTSEED_LOG_TYPE_:
            sys.stderr.write(u"日志类型参数必须为{0}其中一个".format(_IOTSEED_LOG_TYPE_))
            return None
        if self.__type == 'CONSOLE':
            handler = logging.StreamHandler(sys.stdout)
        elif self.__type == 'DAILY':
            if not path:
                sys.stderr.write(u'Daily日志必须设定路径')
            handler = logging.handlers.TimedRotatingFileHandler(path, when='D', backupCount=30, encoding='utf-8')
        elif self.__type == 'ROTATED':
            if not path:
                sys.stderr.write(u'回滚日志必须设定路径')
            handler = logging.handlers.RotatingFileHandler(path, maxBytes=5 * 1024, backupCount=30, encoding='utf-8')
        if handler:
            handler.setFormatter(logging.Formatter('%(message)s'))
            _logger.addHandler(handler)
        return _logger

    def write(self, msg, lvl):
        if lvl == 'Info':
            self._logger.info(msg)
        elif lvl == 'Warn':
            self._logger.warning(msg)
        elif lvl == 'Err':
            self._logger.error(msg)
        elif lvl == 'Critical':
            self._logger.critical(msg)

