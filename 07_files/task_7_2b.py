# -*- coding: utf-8 -*-
"""
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""


file = open("config_sw1.txt")
file_output = open("config_sw1_cleared.txt", "w")
ignore = ["duplex", "alias", "Current configuration"]

for line in file:
    ignore_state = False
    
    for i in ignore:
        if i in line:
            ignore_state = True
    
    if not ignore_state:
        file_output.write(line)

file.close()
file_output.close()
