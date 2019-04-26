#!/usr/bin/python
# -*- coding: UTF-8 -*-
# mydict = {}
# print(mydict)   #输出  {}
# mydict[1] = 'value1'
# mydict['2'] = 'value2'
# print(mydict)  #输出  {1: 'value1', '2': 'value2'}

# #输出  {'name1': 'value1', 'name2': 'value2'}
# mydict2 = {"name1": "value1", "name2": "value2"}
# print(mydict2)


name = ['first', 'google']
mydict3 = dict([name])  #如果name列表中的数据超过两个，这种方法就不能用了。
print(mydict3)  #输出  {'first': 'google'}