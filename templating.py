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

##########################################################################
import re as _re


class _multimap:
    """Helper class for combining multiple mappings.

    Used by .{safe_,}substitute() to combine the mapping and keyword
    arguments.
    """

    def __init__(self, primary, secondary):
        self._primary = primary
        self._secondary = secondary

    def __getitem__(self, key):
        try:
            return self._primary[key]
        except KeyError:
            return self._secondary[key]


class _TemplateMetaclass(type):
    pattern = r"""
    %(delim)s(?:
      (?P<escaped>%(delim)s) |   # Escape sequence of two delimiters
      (?P<named>%(id)s)      |   # delimiter and a Python identifier
      {(?P<braced>%(id)s)}   |   # delimiter and a braced identifier
      (?P<invalid>)              # Other ill-formed delimiter exprs
    )
    """

    def __init__(cls, name, bases, dct):
        super(_TemplateMetaclass, cls).__init__(name, bases, dct)
        if 'pattern' in dct:
            pattern = cls.pattern
        else:
            pattern = _TemplateMetaclass.pattern % {
                'delim': _re.escape(cls.delimiter),
                'id': cls.idpattern,
            }
        cls.pattern = _re.compile(pattern, _re.IGNORECASE | _re.VERBOSE)


class Template:
    """A string class for supporting $-substitutions."""
    __metaclass__ = _TemplateMetaclass

    delimiter = '@'
    idpattern = r'[_a-z][_a-z0-9]*'

    def __init__(self, template):
        self.template = template

    # Search for $$, $identifier, ${identifier}, and any bare $'s

    def _invalid(self, mo):
        i = mo.start('invalid')
        lines = self.template[:i].splitlines(True)
        if not lines:
            colno = 1
            lineno = 1
        else:
            colno = i - len(''.join(lines[:-1]))
            lineno = len(lines)
        raise ValueError('Invalid placeholder in string: line %d, col %d' %
                         (lineno, colno))

    def substitute(*args, **kws):
        if not args:
            raise TypeError("descriptor 'substitute' of 'Template' object "
                            "needs an argument")
        self, args = args[0], args[1:]  # allow the "self" keyword be passed
        if len(args) > 1:
            raise TypeError('Too many positional arguments')
        if not args:
            mapping = kws
        elif kws:
            mapping = _multimap(kws, args[0])
        else:
            mapping = args[0]

        # Helper function for .sub()
        def convert(mo):
            # Check the most common path first.
            named = mo.group('named') or mo.group('braced')
            if named is not None:
                val = mapping[named]
                # We use this idiom instead of str() because the latter will
                # fail if val is a Unicode containing non-ASCII characters.
                return '%s' % (val,)
            if mo.group('escaped') is not None:
                return self.delimiter
            if mo.group('invalid') is not None:
                self._invalid(mo)
            raise ValueError('Unrecognized named group in pattern',
                             self.pattern)

        return self.pattern.sub(convert, self.template)

    def safe_substitute(*args, **kws):
        if not args:
            raise TypeError("descriptor 'safe_substitute' of 'Template' object "
                            "needs an argument")
        self, args = args[0], args[1:]  # allow the "self" keyword be passed
        if len(args) > 1:
            raise TypeError('Too many positional arguments')
        if not args:
            mapping = kws
        elif kws:
            mapping = _multimap(kws, args[0])
        else:
            mapping = args[0]

        # Helper function for .sub()
        def convert(mo):
            named = mo.group('named') or mo.group('braced')
            if named is not None:
                try:
                    # We use this idiom instead of str() because the latter
                    # will fail if val is a Unicode containing non-ASCII
                    return '%s' % (mapping[named],)
                except KeyError:
                    return mo.group()
            if mo.group('escaped') is not None:
                return self.delimiter
            if mo.group('invalid') is not None:
                return mo.group()
            raise ValueError('Unrecognized named group in pattern',
                             self.pattern)

        return self.pattern.sub(convert, self.template)


#################################################################################################

# 暂时写死
def render_template(path, name):
    templates_file = open(path, 'r')
    seq = []
    seq.append(add_author() + '\n')

    for line in templates_file.readlines():
        line = Template(line)
        line = line.safe_substitute(package_name=package_name, entity_list=''.join(get_java_entity_list(name)),
                                    form_list=''.join(get_html_form_list(name)), name=lower_first(name), Name=name,
                                    to2to=to2to(name))
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
                seq = render_template(path, self.g_name)
                out_path = root.replace('templates', 'out/' + self.g_name)
                # 暂时这样定义 java 名称添加生成名称 html不添加生成名称
                if out_path.find('html') > 0:
                    export_file(out_path, name, seq)
                else:
                    export_file(out_path, self.g_name + name, seq)
