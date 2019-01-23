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


def add_author(name):
    author = '''
        /**
          *
          * @author Genesis
          * https://github.com/JohnChancfz/Genesis
          *
          */
        '''
    if name.find('.gtl') > 0:
        return author
    else:
        return '<!-- @author Genesis (https://github.com/JohnChancfz/Genesis) -->\n'


def get_java_package_name(file_name):
    return "package %s.%s;" % (package_name, file_name)


def get_java_extends_base(obj):
    if obj['isExtends']:
        return 'import ' + obj['basePath'] + obj['baseName'] + ';', ' extends ' + obj['baseName']
    else:
        return 'import java.io.Serializable;', ' implements Serializable'


def setter(obj):
    t = get_java_type(obj['type'])
    s = '\t' + 'public void set' + capitalize_first(obj['name']) + '(' + t + ' ' + obj['name'] + ') {this.' + \
        obj['name'] + ' = ' + obj['name'] + ';}' + '\n'
    return s


def getter(obj):
    t = get_java_type(obj['type'])
    s = '\t' + 'public ' + t + ' get' + capitalize_first(obj['name']) + '() {return ' + obj[
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

    entity_seq = get_java_entity_list(array)
    java_seq.extend(entity_seq)

    java_seq.append('}\n')
    return java_seq


def get_java_type(t):
    if t.lower().find('float') >= 0:
        t = 'Float'
    if t.lower().find('double') >= 0:
        t = 'Double'
    if t.lower() in ['string', 'text', 'varchar']:
        t = 'String'
    # if t.lower() == 'int' or t.lower() == 'integer':
    if t.lower().find('int') >= 0:
        t = 'Integer'
    if t.lower().find('decimal') >= 0:
        t = 'java.math.BigDecimal'
    if t.lower() == 'datetime' or t.lower() == 'date':
        t = 'java.util.Date'
    # if t.lower() == 'tinyint':
    #    t = 'Short'
    return t


def get_html_type(t):
    if t.lower().find('float') >= 0 or t.lower().find('double') >= 0 or t.lower().find(
            'decimal') >= 0 or t.lower().find('int') >= 0:
        t = 'number'
    elif t.lower() == 'text':
        t = 'textarea'
    else:
        t = 'text'
    # if t.lower() == 'datetime' or t.lower() == 'date':
    #     t = 'Date'
    # if t.lower() == 'tinyint':
    #    t = 'Short'
    return t


def get_java_entity_list(array=[]):
    print 'get_java_entity_list'
    java_seq = []
    for obj in array:
        name = obj['name']
        t = get_java_type(obj['type'])
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
        else:
            size_str = ''
            if obj['size'] > 0:
                size_str = '(' + str(obj['size']) + ')'
            # column ='nullable = false,'+
            default_str = ''
            if default.lower() != 'null' and default != '':
                default_str = ' default ' + default

            column = 'columnDefinition = "' + obj['type'] + size_str + default_str + '"'
            print column
            # 暂时不添加@Column 有好多特性没有完成
            #java_seq.append('\t' + '@Column(' + column + ')' + '\n')
        java_seq.append('\t' + 'private ' + t + ' ' + name + ';' + '\n\n')
        java_seq.append(getter_and_setter(obj))

    return java_seq


def get_html_form_list(array=[]):
    seq = []
    for obj in array:
        obj_name = obj['name']
        t = get_html_type(obj['type'])
        size = obj['size']
        remark = obj['remark']
        default = obj['default']
        seq.append('\n')

        # 添加\t
        tab = 7 * '\t'
        if obj_name == 'id':
            seq.append(tab + '<input type="hidden" id="id" name="id" value="${bean.id}">' + '\n')
        else:
            seq.append(tab + '<div class="form-group">' + '\n')
            seq.append(tab + '\t' + '<label class="col-sm-3 control-label">' + remark + '</label>' + '\n')
            seq.append(tab + '\t' + '<div class="col-sm-8">' + '\n')
            if t == 'textarea':
                seq.append(tab + '\t\t' +
                           '<textarea id = "' + obj_name + '" name = "' + obj_name + '" class ="form-control" > ${bean.' + obj_name + '} </textarea>' + '\n')
            else:
                seq.append(tab + '\t\t' +
                           '<input id="' + obj_name + '" name="' + obj_name + '" class="form-control" type="' + t + '" value="${bean.' + obj_name + '}"  >' + '\n')
            seq.append(tab + '\t' + '</div>' + '\n')
            seq.append(tab + '</div>' + '\n')

    return seq
