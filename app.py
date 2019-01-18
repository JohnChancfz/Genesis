# -*- coding: utf-8 -*-

'''
    @Author John Chan 'chenfazhun@163.com'
'''
from utils.operatefile import read_file, export_file
from utils.generator import java_entity_generator
import os


class Genesis(object):

    def __init__(self):
        print 'init Genesis ...'

    def run(self):
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
            name = name[:-3]
            # generator entity class
            seq = java_entity_generator(name,array)
            export_file('./out/entity', name + '.java', seq)
