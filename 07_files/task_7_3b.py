# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv

vlan = argv[1]
file = open("CAM_table.txt")

for line in file:
    line_list = line.split()

    try:
        if line_list[0] == vlan:
            print(f" {line_list[0]:7}{line_list[1]:17}{line_list[3]}")

    except IndexError:
        pass

file.close()