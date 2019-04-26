#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
使用Python+selenium登录百度账号。
模块化编程：使用配置文件的方式读取代码中需要的参数信息。
流程：
（1）打开百度首页，点击右上角的“登录”，打开登录对话框==》选择左下角的“用户名登录”==》输入用户名、密码，点击登录按钮。
（2）如果登录失败，则将显示的失败信息写到日志文件中，继续执行其他的测试用例。
（3）如果登录成功，则需要将用户注销，然后再继续执行下面的测试用例。
（4）测试用例：用户的信息（账号，密码）存放在Excel中，网页的元素信息存放在.txt文件中。（目的是为了学两种文件的存取方法）
（5）测试结果：可以存放在.txt文件或者excel中。

webinfo.txt存放的是定位元素需要的参数信息==》最终需要的是字典的形式，一个参数对应字典中的一个参数。
userinfo.txt存放的是用户的信息：用户名和密码==》最终需要的是列表，列表中存在多个字典，每个字典对应一个用户名和密码（即文本中的一行）

'''
# import sys
# sys.path.append('D:\PycharmProjects\Demo1\config')
# 加上上述两句话，才能把自己定义的不在同一个包下的包引进来
# print(sys.path)
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
from config.InfoConfig import get_webInfo,get_userInfo
from LoginBaidu.LogModule import Loginfo, Xlloginfo
from selenium.webdriver.common.action_chains import ActionChains
from LoginBaidu.ExcelConfig import XlUserinfo
# 等待时间函数，可以不用
def get_ele_times(driver, times, func):
    return WebDriverWait(driver, times).until(func)

# 打开浏览器
def openBrower():
    webdriver_handle = webdriver.Chrome()
    return webdriver_handle

# 打开具体的网页
def openUrl(handle, url):
    handle.get(url)
    handle.maximize_window()

# 定位元素
def findElement(driver, args):
    if 'text_id' in args:
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_link_text(args['text_id'])).click()
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(args['username_id'])).click()
    userEle = driver.find_element_by_id(args['user_id'])
    pwdEle = driver.find_element_by_id(args['pwd_id'])
    loginEle = driver.find_element_by_id(args['login_id'])
    return userEle, pwdEle, loginEle

# 异常处理
#将测试结果写到.txt文件中，详见LogModule.py
def checkResult(driver, err_id, arg, log):
    result_flag = False  #用来标记登录的结果，成功为true
    # time.sleep(2)
    try:
        err = driver.find_element_by_id(err_id)
        print('err.text:', err.text)
        # print('errro:', result_flag)
        # msg = '%s,%s : error:%s\n'%(arg['username'],arg['password'], err.text)
        # log.log_write(msg)
        log.log_write(arg['username'], arg['password'], 'Error', err.text)

    except:
        print("账号和密码正确")
        # msg = '%s:pass\n'%(arg)
        # log.log_write(msg)
        log.log_write(arg['username'], arg['password'], 'Pass')
        result_flag = True
    print(result_flag)
    return result_flag

#给定位的元素发送数值
def sendVals(ele_tuple, arg):
    listkey = ['username', 'password']
    i = 0
    for key in listkey:
        ele_tuple[i].send_keys('')
        ele_tuple[i].clear()
        ele_tuple[i].send_keys(arg[key])
        i += 1
    time.sleep(2)
    ele_tuple[2].click()

#注销登录，为了测试下一条用例
def logout(brower, ele_dict):
    ele = brower.find_element_by_id(ele_dict['logout'])
    ActionChains(brower).move_to_element(ele).perform()
    brower.find_element_by_link_text(ele_dict['dropout']).click() #这里会出一个对话框，让确定是否退出
    brower.switch_to.alert.accept()

# 登录测试总函数
def login_test(ele_dict, user_list):
    brower = openBrower()
    #log = Loginfo()
    log = Xlloginfo()
    log.log_init('sheet1', 'username', 'password', 'result', 'info')
    openUrl(brower, ele_dict['url'])
    ele_tuple = findElement(brower, ele_dict)
    for arg in user_list:  #user_list中可能有很多组账号和密码，故要用循环
        sendVals(ele_tuple, arg)
        result_flag = checkResult(brower, ele_dict['errorid'], arg, log)
        if result_flag:  #如果已经登录成功，则需要注销后重新登录
            logout(brower, ele_dict)
            ele_tuple = findElement(brower, ele_dict)
    # ele_tuple[0].send_keys(user_list[0]['username'])
    # ele_tuple[1].send_keys(user_list[0]['password'])
    # ele_tuple[2].click()
    log.log_close()


if __name__ == '__main__':
    '''
    #第一种方法：直接在程序中给出登录网站需要的用户信息和需要定位的元素信息
    
    url = 'http://www.baidu.com'
    login_text = '登录'
    username = '####'
    password = '#####'
    # ele_dict是字典
    ele_dict = {'url': url, 'text_id': login_text,
                'user_id': 'TANGRAM__PSP_10__userName',
                'pwd_id': 'TANGRAM__PSP_10__password',
                'login_id': 'TANGRAM__PSP_10__submit',
                'username_id': 'TANGRAM__PSP_10__footerULoginBtn',
                'errorid': 'TANGRAM__PSP_10__error'}
    
    # user_list是列表，列表里面是字典，每一个用户名和密码对应一个字典。
    user_list = [{'username': username, 'password': username}]  
   
    '''

    '''
    第二种方法：将需要的用户信息和定位元素的参数写在配置文件中（.txt），从里面读取相应的信息。
    ele_dict = get_webInfo('D:\PycharmProjects\Demo1\config\webinfo.txt')
    user_list = get_userInfo('D:\PycharmProjects\Demo1\config\\userinfo.txt')
    
    '''

    '''
    第三种方法：把用户信息放在Excel文件中
    '''
    ele_dict = get_webInfo('D:\PycharmProjects\Demo1\config\webinfo.txt')
    # user_list = get_userInfo('D:\PycharmProjects\Demo1\config\\userinfo.txt')

    user_list = XlUserinfo('D:\PycharmProjects\Demo1\LoginBaidu\\userinfo_result.xlsx').get_sheetinfo_by_index(0)
    login_test(ele_dict, user_list)

    time.sleep(5)  # 防止程序执行完接着把浏览器关掉