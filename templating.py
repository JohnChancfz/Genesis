# -*- coding: utf-8 -*-

'''
    code generator
    @Author John Chan 'chenfazhun@163.com'
'''

from config import package_name
from utils.string_utils import lower_first, to2to
from utils.operatefile import export_file
from utils.generator import add_author, get_java_entity_list, get_html_form_list
import os


def template(path, name):
    templates_file = open(path, 'r')
    seq = []
    seq.append(add_author() + '\n')
    for line in templates_file.readlines():
        line = line.replace('--to2to--', to2to(name)).replace('--package_name--', package_name).replace('--name--',
                                                                                                        name).replace(
            '--lower_name--',
            lower_first(name))
        if line.find('--entity_list--') >= 0:
            seq.extend(get_java_entity_list(name))
        elif line.find('--form_list--') >= 0:
            seq.extend(get_html_form_list(name))
        else:
            seq.append(line)
    return seq


class Templates(object):

    def __init__(self, g_name, path='./templates'):
        print 'Templates init'
        self.g_name = g_name
        self.path = path

    def render(self):

        for root, dirs, files in os.walk(self.path):
            # print 'root = ', root
            # print 'dirs = ', dirs
            # print files
            for name in files:

                path = os.path.join(root, name)
                seq = template(path, self.g_name)
                out_path = root.replace('templates', 'out/' + self.g_name)
                # 暂时这样定义 java 名称添加生成名称 html不添加生成名称
                if out_path.find('html') > 0:
                    export_file(out_path, name, seq)
                else:
                    export_file(out_path, self.g_name + name, seq)
