# -*- coding: utf-8 -*-

'''
    code generator
    @Author John Chan 'chenfazhun@163.com'
'''

from config import package_name, entity
from string_utils import capitalize_first, lower_first, to2to
from utils.operatefile import read_file
import os

def generator():
    print ''


def add_author():
    author = '''
    /**
      *
      * @author Genesis
      * https://github.com/JohnChancfz/Genesis
      *
      */
    '''
    return author


def get_java_package_name(file_name):
    return "package %s.%s;" % (package_name, file_name)


def get_java_extends_base(obj):
    if obj['isExtends']:
        return 'import ' + obj['basePath'] + obj['baseName'] + ';', ' extends ' + obj['baseName']
    else:
        return 'import java.io.Serializable;', ' implements Serializable'


def setter(obj):
    s = '\t' + 'public void set' + capitalize_first(obj['name']) + '(' + obj['type'] + ' ' + obj['name'] + ') {this.' + \
        obj['name'] + ' = ' + obj['name'] + ';}' + '\n'
    return s


def getter(obj):
    s = '\t' + 'public ' + obj['type'] + ' get' + capitalize_first(obj['name']) + '() {return ' + obj[
        'name'] + ';}' + '\n\n'
    return s


def getter_and_setter(obj):
    return getter(obj) + setter(obj)


def java_entity_generator(name, array, isExtends=False):
    java_seq = []

    java_seq.append(get_java_package_name(entity['fileName']) + '\n\n')

    ei, en = get_java_extends_base(entity)
    # import class
    java_seq.append(ei + '\n')
    java_seq.append('import javax.persistence.*;\n')

    java_seq.append(add_author() + '\n')

    java_seq.append('@Entity\n')
    java_seq.append('@Table(name = "genesis_' + to2to(name) + '")\n')
    java_seq.append('public class ' + name + en + '{' + '\n')

    entity_seq = get_java_entity_list(name)
    java_seq.extend(entity_seq)

    java_seq.append('}\n')
    return java_seq

def get_java_entity_list(name):
    java_seq = []
    path = os.path.join('./files', name+'.md')
    array = read_file(path)
    for obj in array:
        name = obj['name']
        t = obj['type']
        size = obj['size']
        remark = obj['remark']
        default = obj['default']
        java_seq.append('\n')
        java_seq.append('\t' + '// ' + remark + '\n')
        if name == 'id':
            java_seq.append('\t' + '@Id' + '\n')
            # GenerationType
            if default == 'auto':
                java_seq.append('\t' + '@GeneratedValue(strategy = GenerationType.AUTO)' + '\n')
            java_seq.append('\t' + '@Column(name = "id", nullable = false)' + '\n')
        java_seq.append('\t' + 'private ' + t + ' ' + name + ';' + '\n\n')
        java_seq.append(getter_and_setter(obj))

    return java_seq

