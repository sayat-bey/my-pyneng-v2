# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""


from sys import argv

file_argv = argv[1]
file = open(file_argv)
ignore = ["duplex", "alias", "Current configuration"]

for line in file:
    ignore_state = False
    if not line.startswith("!"):
    
        for i in ignore:
            if i in line:
                ignore_state = True
        
        if not ignore_state:
            print(line.rstrip())

file.close()