#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
日志接口:
    把测试用例执行的结果存储在文件中
    格式： 用户名，密码：测试结果
'''

import time
import xlsxwriter
'''将测试结果写到.txt文本中'''
class Loginfo(object):
    #打开日志文件
    def __init__(self, path='', mode='w'):  #path默认是当前目录
        # fname = path + time.strftime('%Y-%m-%d', time.gmtime())
        fname = path + time.strftime("%Y-%m-%d %H_%M_%S", time.localtime(time.time()))
        self.log = open(path + fname + '.txt', mode)

    #把执行结果保存到日志文件中
    def log_write(self, msg):
        self.log.write(msg)

    #关闭日志文件
    def log_close(self):
        self.log.close()


'''将测试结果写到Excel中'''
class Xlloginfo(object):
    def __init__(self, path=''):
        fname = path + time.strftime("%Y-%m-%d %H_%M_%S", time.localtime(time.time()))
        self.row = 0
        self.xl = xlsxwriter.Workbook(path+fname+'.xlsx')   #新建一个excel文件
        self.style = self.xl.add_format({'color': 'red'})  #对输出结果是Error的类型，设置字体的颜色为红色

    def log_init(self, sheetname, *title):
        self.sheet = self.xl.add_worksheet(sheetname) #新建一个sheet
        self.sheet.set_column('A:E', 30) #设置单元格的宽度
        self.log_write(*title)

    def log_write(self, *args):
        col = 0
        style = ''
        if 'Error' in args:
            style = self.style
        for val in args:
            self.sheet.write_string(self.row, col, val, style)
            col += 1
        self.row += 1

    def log_close(self):
        self.xl.close()


if __name__ == '__main__':
    # log = Loginfo()
    # log.log_write('test Loginfo 测试')
    # log.log_close()
    xinfo = Xlloginfo()
    xinfo.log_init('test', 'username', 'password', 'result', 'info')
    xinfo.log_write('123', '123', 'Error', 'error')
    xinfo.log_close()