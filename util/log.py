# coding=utf-8
import logging
import logging.handlers

class FinalLogger:

    logger = None

    levels = {"n" : logging.NOTSET,
              "d" : logging.DEBUG,
              "i" : logging.INFO,
              "w" : logging.WARN,
              "e" : logging.ERROR,
              "c" : logging.CRITICAL}

    log_level = "w"
    log_file = "running.log"
    log_max_byte = 10 * 1024 * 1024;
    log_backup_count = 5

    @staticmethod
    def getLogger():
        if FinalLogger.logger is not None:
            return FinalLogger.logger

        FinalLogger.logger = logging.getLogger('')
        # FinalLogger.logger = logging.Logger('Logging')

        #   把log信息输入到文件中
        log_file_handler = logging.handlers.RotatingFileHandler(filename = FinalLogger.log_file, \
                                                           maxBytes = FinalLogger.log_max_byte, \
                                                           backupCount = FinalLogger.log_backup_count)
        #   在控制台输出log信息
        log_console_handler = logging.StreamHandler()

        #   输出的格式
        formater = logging.Formatter("[%(asctime)s]-[%(filename)s]-[%(funcName)s]-[%(levelname)s]-%(message)s")
        log_file_handler.setFormatter(formater)
        log_console_handler.setFormatter(formater)

        #   添加handler到logger中
        FinalLogger.logger.addHandler(log_file_handler)
        FinalLogger.logger.addHandler(log_console_handler)

        #   设置log的级别，默认为debug
        FinalLogger.logger.setLevel(FinalLogger.levels.get(FinalLogger.log_level))

        #   返回一个logger对象
        return FinalLogger.logger

if __name__ == "__main__":
    logger = FinalLogger.getLogger()
    logger.debug("this is a debug msg!")
    logger.info("this is a info msg!")
    logger.warn("this is a warn msg!")
    logger.error("this is a error msg!")
    logger.critical("this is a critical msg!")





