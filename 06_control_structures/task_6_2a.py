# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Сообщение должно выводиться только один раз.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ipadd = input("Enter IP address (10.0.1.1): ")

iplist = ipadd.split(".")
ipcorrect = True

while ipcorrect:
    
    if len(iplist) == 4:
        for ip in iplist:
            if 0<= int(ip) <=255:
                continue
            else:
                ipcorrect = False
                break
        break
    else:
        ipcorrect = False


if ipcorrect:

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
            
else:
    print("Неправильный IP-адрес")