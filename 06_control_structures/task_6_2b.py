# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""






while True:

    ipadd = input("Enter IP address (10.0.1.1): ")

    iplist = ipadd.split(".")
    
    if len(iplist) == 4:
        for ip in iplist:
            if 0<= int(ip) <=255:
                continue
            else:
                print("Неправильный IP-адрес")
                break
        else:
            break
    else:
        print("Неправильный IP-адрес")


ip1 = iplist[0]

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
        
