# -*- coding: utf-8 -*-
"""
Задание 4.5

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2 (пересечение).

Результатом должен быть такой список: ['1', '3', '8']

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"

command1_vlan = command1.split()[-1].split(',')
command2_vlan = command2.split()[-1].split(',')

intersection_vlan = set(command1_vlan).intersection(set(command2_vlan))

intersection_list = list(intersection_vlan)

print(intersection_list)