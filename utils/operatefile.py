# -*- coding: utf-8 -*-

'''
    code generator
    @Author cfz
'''

import os


class OperateFile(object):

    def __init__(self, path, out_path):
        self.path = path
        self.out_path = out_path

    def read_file(self, name):
        md_file = open(self.path + os.sep + name)
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

    def export_file(self, name,seq):
        java_file = open("./out/entity/Item.java", 'w')
        java_file.writelines(seq)
        java_file.close()



def get_java_type(t):
    if t.lower() == 'double':
        t = 'Double'

    if t.lower() in ['string', 'text', 'varchar']:
        t = 'String'

    if t.lower() == 'int' or t.lower() == 'integer':
        t = 'Integer'
    return t


def run():
    of = OperateFile('./files', './out')
    seq = of.read_file("Item.md")

    from utils.generator import java_generator
    java_seq = java_generator(seq)
    of.export_file('Item.java',java_seq)

