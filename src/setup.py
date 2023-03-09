#!/bin/python3
import os

# 获取文件列表
files = os.listdir('SL')
files.remove('__init__.py')

# 生成一个新的文件
with open('SL.py', 'wt', encoding='utf-8') as fp:
    for i in files:
        if i.endswith('.py'):
            with open(os.path.join('SL',i), 'rt', encoding='utf-8') as pyfp:
                text = pyfp.read()
                text = text[text.find('# start\n') + 8:]
                fp.write(text + '\n')

