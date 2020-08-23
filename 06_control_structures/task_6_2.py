# -*- coding: utf-8 -*-
"""
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить тип IP-адреса.
3. В зависимости от типа адреса, вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ipadd = input("Enter IP address (10.0.1.1): ")

ip1 = ipadd.split(".")[0]

if 1 <= int(ip1) <= 223:
    print('unicast')
    
elif 224 <= int(ip1) <= 239:
    print('multicast')

else:
    if ipadd == "255.255.255.255":
        print("local broadcast")
    elif ipadd == "0.0.0.0":
        print("unassigned")
    else:
        print("unused")