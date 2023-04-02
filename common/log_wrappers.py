# python3
# @File: log.py
# --coding:utf-8--
# @Author:axjing
# @Time: 2021年09月16日17
# 说明:
import sys
import logging
import time
import os


class Logging(object):
    """
    Log输出标注设置
    """

    def __init__(self, logger=None, log_cate='log_run'):
        """
        指定保存日志的文件路径，日志级别，以及调用文件。将日志存入到指定的文件中
        :param logger:调用模块名，一般输入__name__
        :param log_cate:指定存放的log名
        """
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        # 创建一个handler，用于写入日志文件
        self.log_time = time.strftime("%Y_%m_%d")
        file_dir = os.path.join(os.getcwd(), '../log')
        if not os.path.exists(file_dir):
            os.mkdir(file_dir)
        self.log_path = file_dir
        self.log_filename = os.path.join(self.log_path, log_cate + "_" + self.log_time + '.log')

        # 定义handler的输出格式
        self.formatter = logging.Formatter(
            '[%(asctime)s] PID:%(process)d %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s] %(message)s')
        file_hdl = self.get_file_handler(self.log_filename)
        csl_hdl = self.get_console_handler()
        self.logger.addHandler(file_hdl)
        self.logger.addHandler(csl_hdl)

        file_hdl.close()
        csl_hdl.close()

    def get_logger(self):
        return self.logger

    def get_file_handler(self, filename):
        """
        输出到文件handler的函数定义
        :param filename:指定存放的log名
        :return:文件handler的函数对象
        """
        filehandler = logging.FileHandler(filename, encoding="utf-8")
        filehandler.setFormatter(self.formatter)
        return filehandler

    def get_console_handler(self):
        """
        输出到控制台handler的函数定义
        :return:控制台handler的函数对象
        """
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(self.formatter)
        return console_handler


if __name__ == "__main__":
    logger = Logging(__name__).get_logger()

    logger.info("==========\n")
