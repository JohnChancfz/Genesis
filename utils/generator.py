# -*- coding: utf-8 -*-

'''
    code generator
    @Author cfz
'''

def generator():
    print ''

def java_generator(seq):
    java_seq = []
    for obj in seq:
        name = obj['name']
        t = obj['type']
        size = obj['size']
        remark = obj['remark']
        default = obj['default']
        java_seq.append('\n')
        java_seq.append('// ' + remark + '\n')
        if name == 'id':
            java_seq.append('@Id' + '\n')
            java_seq.append('@GeneratedValue(strategy = GenerationType.AUTO)' + '\n')
            java_seq.append('@Column(name = "id", nullable = false)' + '\n')

        java_seq.append('private ' + t + ' ' + name + ';' + '\n')

    return java_seq
