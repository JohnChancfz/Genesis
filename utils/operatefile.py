# -*- coding: utf-8 -*-

'''
    code generator
    @Author John Chan 'chenfazhun@163.com'
'''

import os


def read_file(path):
    md_file = open(path, 'r')
    seq = []
    # line no
    i = 0
    for line in md_file.readlines():
        i = i + 1
        if i <= 3:
            continue
        elements = line.split("|")
        name = elements[0].strip()
        t = elements[1].strip()
        if t.find("(") > 0:
            t1 = t[:t.find("(")]
            t2 = t[t.find("(") + 1:-1]
        else:
            t1 = t
            t2 = 0
        default = elements[2].strip()
        remark = elements[3].strip()

        t1 = get_java_type(t1)

        obj = {"name": name, "type": t1, "size": t2, "default": default, "remark": remark}
        seq.append(obj)

    md_file.close()
    return seq


def export_file(path, name, seq):
    if not os.path.exists(path):
        os.makedirs(path)
    java_file = open(path + os.sep + name, 'w')
    java_file.writelines(seq)
    java_file.close()


def get_java_type(t):
    if t.lower() == 'float':
        t = 'Float'
    if t.lower() == 'double':
        t = 'Double'
    if t.lower() in ['string', 'text', 'varchar']:
        t = 'String'
    if t.lower() == 'int' or t.lower() == 'integer':
        t = 'Integer'
    if t.lower() == 'datetime' or t.lower() == 'date':
        t = 'Date'
    if t.lower() == 'tinyint':
        t = 'Short'
    return t
