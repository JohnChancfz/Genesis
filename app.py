# -*- coding: utf-8 -*-

'''
    @Author John Chan 'chenfazhun@163.com'
'''
from utils.operatefile import read_file, export_file
from utils.generator import java_entity_generator
from templating import Templates
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

            #seq = java_entity_generator(name, array)
            #export_file('./out/'+name+'/entity', name + 'Entity.java', seq)
            # # generator dao class
            # seq = template('./templates/dao/INameDao.java', name)
            # export_file('./out/dao', 'I'+name + 'Dao.java', seq)
            #
            # # generator service class
            # seq = template('./templates/service/INameService.java', name)
            # export_file('./out/service', 'I' + name + 'Service.java', seq)
            #
            # # generator service impl class
            # seq = template('./templates/service/impl/NameServiceImpl.java', name)
            # export_file('./out/service/impl',  name + 'ServiceImpl.java', seq)

            template = Templates(g_name=name)
            template.render()

