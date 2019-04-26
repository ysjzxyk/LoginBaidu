#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xlrd
# xl = xlrd.open_workbook('D:\PycharmProjects\Demo1\LoginBaidu\\userinfo_result.xlsx')
# table = xl.sheets()[0]
# count_row = table.nrows #总行数
# print('count_row:', count_row)
# user_info = []
# for row in range(1, count_row):
#     user_dict = {}
#     row_result = table.row_values(row)
#     user_dict.update(dict([row_result]))
#     user_info.append(user_dict)
# print(user_info)

class XlUserinfo(object):
    def __init__(self, path=''):
        self.xl = xlrd.open_workbook(path) #打开Excel

    '''
    如果Excel表格中是纯数字的单元格，获取后会把int类型的自动变成float类型的。解决方法有两种：
    （1）把Excel中的单元格格式改为“文本”格式，这边就可以正常获取
    （2）利用下面的floattostr()方法，把float转换为字符串
    '''
    # 这个方法是把float再转换成int，再转化为字符串
    def floattostr(self, val):
        if isinstance(val, float): #isinstance()函数来判断一个对象是否是一个已知的类型
            val = str(int(val))
        return val

    # 通过名称获取表格
    def get_sheetinfo_by_name(self, name):
        self.sheet = self.xl.sheet_by_name(name)
        return self.get_sheet_info()

    # 通过索引获取表格
    def get_sheetinfo_by_index(self, index):
        self.sheet = self.xl.sheet_by_index(index)
        return self.get_sheet_info()

    # 得到某一个数据表中的所有数据
    def get_sheet_info(self):
        count_row = self.sheet.nrows # 总行数
        print('count_row:', count_row)
        userlist_key = ['username', 'password']
        user_info = []
        for row in range(1, count_row):
            # row_result = self.sheet.row_values(row)
            info = [self.floattostr(val) for val in self.sheet.row_values(row)]
            row_result = zip(userlist_key, info)
            # print('row_result:', row_result)
            user_info.append(dict(row_result))
        return user_info


if __name__ == '__main__':
    xinfo = XlUserinfo('D:\PycharmProjects\Demo1\LoginBaidu\\userinfo_result.xlsx')
    info = xinfo.get_sheetinfo_by_index(0)
    print('info1:', info)
    # info = xinfo.get_sheetinfo_by_name('Sheet1')
    # print('info2:', info)


