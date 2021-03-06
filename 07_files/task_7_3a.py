# -*- coding: utf-8 -*-
"""
Задание 7.3a

Сделать копию скрипта задания 7.3.

Дополнить скрипт:
- Отсортировать вывод по номеру VLAN

В результате должен получиться такой вывод:
10       01ab.c5d0.70d0      Gi0/8
10       0a1b.1c80.7000      Gi0/4
100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
300      a2ab.c5a0.700e      Gi0/3
500      02b1.3c80.7b00      Gi0/5
1000     0a4b.c380.7d00      Gi0/9

Обратите внимание на vlan 1000 - он должен выводиться последним.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from pprint import pprint

file = open("CAM_table.txt")
output = []

for line in file:
    line_list = line.split()

    try:
        if line_list[0].isdigit():
            output.append([int(line_list[0]), line_list[1], line_list[3]])

    except IndexError:
        pass

output.sort()

for i in output:
    print(f" {i[0]:<7}{i[1]:17}{i[2]}")

file.close()
