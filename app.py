# -*- coding: utf-8 -*-
from utils.operatefile import read_file, export_file
from utils.generator import java_generator
import os


class Genesis(object):

    def __init__(self):
        print 'init Genesis ...'

    def run(self):
        # files = os.listdir(MD_PATH)
        # of = OperateFile(MD_PATH, OUT_PATH)
        # seq = of.read_file("Item.md")
        #
        # from utils.generator import java_generator
        # java_seq = java_generator(seq)
        # of.export_file('Item.java', java_seq)

        # for root, dirs, files in os.walk('./files'):
        #     print root
        #     print dirs
        #     print files
        #     for name in files:
        #         print name
        print 'Genesis run ...'
        for name in os.listdir('./files'):
            path = os.path.join('./files', name)
            array = read_file(path)
            seq = java_generator(array)
            export_file('./out', seq)
