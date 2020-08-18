# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_mask = input("Enter IP address (10.1.1.0/24): ")

ip, mask = ip_mask.split("/")

oc1, oc2, oc3, oc4 = ip.split(".")
maskb = "1"*int(mask) + "0"*(32-int(mask))
mask1 = maskb[0:8]
mask2 = maskb[8:16]
mask3 = maskb[16:24]
mask4 = maskb[24:]

result = f'''
Network:
{oc1:10}{oc2:10}{oc3:10}{oc4:10}
{int(oc1):08b}  {int(oc2):08b}  {int(oc3):08b}  {int(oc4):08b}

Mask:
/{mask}
{int(mask1,2):<10}{int(mask2,2):<10}{int(mask3,2):<10}{int(mask4,2):<10}
{mask1:10}{mask2:10}{mask3:10}{mask4:10}
'''




print(result)