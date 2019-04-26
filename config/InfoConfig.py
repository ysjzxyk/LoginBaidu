#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
用于获取多种文件格式的文件内容的接口
（1）get_webInfo()：获取.txt文件的内容，结果是一个字典
（2）get_userInfo()：获取.txt文件的内容，结果是一个列表，列表中每一个元素是一个字典，文件中的一行对应一个字典。
（3）class XlUserinfo(object)：从Excel中读取用户信息
'''
import xlrd
def get_webInfo(path):
    web_info = {}
    config = open(path) #返回的是一个IOtextwrapper类型，按照行数来迭代。
    #print(config.read()) #read()返回的是字符串，它是按照一个一个字来迭代的。
    for line in config:
        #result = line.split('=')[1].strip()
        result = [ele.strip() for ele in line.split('=')]#split返回的是字符串列表。如{'text_id'，'登录'}
        #print(result)
        web_info.update(dict([result])) #可以用dict([result])创建一个字典，结果如：{'text_id': '登录'}
    return web_info

def get_userInfo(path):
    user_info = []
    config = open(path)
    for line in config:
        user_dict = {}
        result = [ele.strip() for ele in line.split(';')] #分割后是：username=***和password=***
        for u in result:
            u_result = [ele.strip() for ele in u.split('=')]
            print('u_result:', u_result)
            user_dict.update(dict([u_result]))
        user_info.append(user_dict)
    return user_info

#从Excel中读取用户信息
# class XlUserinfo(object):
def get_sheet_info(path):
    xl = xlrd.open_workbook(path)
    table = xl.sheets()[0]
    count_row = table.nrows  # 总行数
    # print('count_row:', count_row)
    user_info = []
    for row in range(1, count_row):
        user_dict = {}
        row_result = table.row_values(row)
        user_dict.update(dict([row_result]))
        user_info.append(user_dict)
    return user_info


if __name__ == '__main__':
    # info = get_webInfo('D:\PycharmProjects\Demo1\config\webinfo.txt')
    # for key in info:
    #     print(key, info[key])

    user_info2 = get_userInfo('D:\PycharmProjects\Demo1\config\\userinfo.txt')
    print(user_info2)
    # for key1 in user_info2:
    #     print(key1, user_info2[key1])


    # user_list = get_userInfo('D:\PycharmProjects\Demo1\config\\userinfo.txt')
    # print(user_list)


