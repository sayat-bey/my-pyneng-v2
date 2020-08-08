# -*- coding: utf-8 -*-
"""
Задание 4.3

Получить из строки config такой список VLANов:
['1', '3', '10', '20', '30', '100']

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

config = "switchport trunk allowed vlan 1,3,10,20,30,100"

vlans = config.split("vlan")[1].strip()

vlans_list = vlans.split(",")

print(vlans_list)


###

vlans_2 = config.split()[-1]
vlans_list_2 = vlans.split(",")

print(vlans_list_2)