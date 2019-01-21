# -*- coding: utf-8 -*-

'''
    @Author John Chan 'chenfazhun@163.com'
'''
from utils.operatefile import read_file, export_file
from utils.generator import add_author, get_html_form_list, get_java_entity_list
from templating import Template, Templates

from config import package_name
from utils.string_utils import lower_first, to2to
import os


class Genesis(object):

    def __init__(self, path='./files', out_path='./out'):
        print 'init Genesis ...'
        self.path = path
        self.out_path = out_path

    def run(self):
        print 'Genesis run ...'

        for name in os.listdir(self.path):
            path = os.path.join(self.path, name)
            array = read_file(path)
            name = name[:-3]

            template = Templates()
            # template.render()
            templates = template.get_template_array()

            for t in templates:
                out_path = t['root'].replace('templates', 'out/' + name)
                print out_path
                out_name = t['name']
                print out_name
                seq = []
                seq.append(add_author() + '\n')
                for line in t['content']:
                    line = Template(line)
                    line = line.safe_substitute(package_name=package_name,
                                                entity_list=''.join(get_java_entity_list(array)),
                                                form_list=''.join(get_html_form_list(array)), name=lower_first(name),
                                                Name=name,
                                                to2to=to2to(name))
                    seq.append(line)

                # 暂时这样定义 java 名称添加生成名称 html不添加生成名称
                if out_path.find('html') > 0:
                    export_file(out_path, out_name, seq)
                else:
                    export_file(out_path, name + out_name, seq)
