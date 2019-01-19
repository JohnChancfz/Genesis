# -*- coding: utf-8 -*-

'''
    code generator
    @Author John Chan 'chenfazhun@163.com'
'''


def capitalize_first(str):
    return str[0].upper() + str[1:]


def lower_first(str):
    return str[0].lower() + str[1:]


# 写的好水 请原谅我
def to2to(str):
    ss = ''
    for s in str[1:]:
        if s.isupper():
            s = '_' + s.lower()
        ss = ss + s

    return str[0].lower() + ss