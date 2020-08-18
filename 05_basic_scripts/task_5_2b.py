# -*- coding: utf-8 -*-
"""
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv

mask = argv[1]
ip = input("Enter IP address (10.1.1.0): ")

oc1, oc2, oc3, oc4 = ip.split(".")
ipbin = f"{int(oc1):08b}{int(oc2):08b}{int(oc3):08b}{int(oc4):08b}"

networkbin = ipbin[0:int(mask)] + "0"*(32-int(mask))
ip1 = networkbin[0:8]
ip2 = networkbin[8:16]
ip3 = networkbin[16:24]
ip4 = networkbin[24:]

maskb = "1"*int(mask) + "0"*(32-int(mask))
mask1 = maskb[0:8]
mask2 = maskb[8:16]
mask3 = maskb[16:24]
mask4 = maskb[24:]

result = f'''
Network:
{int(ip1,2):<10}{int(ip2,2):<10}{int(ip3,2):<10}{int(ip4,2):<10}
{ip1:10}{ip2:10}{ip3:10}{ip4:10}

Mask:
/{mask}
{int(mask1,2):<10}{int(mask2,2):<10}{int(mask3,2):<10}{int(mask4,2):<10}
{mask1:10}{mask2:10}{mask3:10}{mask4:10}
'''




print(result)