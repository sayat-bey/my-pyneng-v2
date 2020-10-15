# -*- coding: utf-8 -*-
"""
Задание 12.3


Создать функцию print_ip_table, которая отображает таблицу доступных и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

Функция не должна изменять списки, которые переданы ей как аргументы.
То есть, до выполнения функции и после списки должны выглядеть одинаково.


Для этого задания нет тестов
"""


def print_ip_table(reachable, unreachable):

    max_len = max(len(reachable), len(unreachable))
    min_len = min(len(reachable), len(unreachable))
    
    print("Reachable    Unreachable")
    print("-----------  -------------")
    
    i = 0
    while i < max_len:
        if i < min_len:
            print(f"{reachable[i]:13}{unreachable[i]}")
            
        else:
            if len(reachable) > len(unreachable):
                print(f"{reachable[i]}")
            else:
                print(f"{'':13}{unreachable[i]}")
                
        i += 1
        
reachable = ("10.1.1.1", "10.1.1.2", "10.1.1.3", "10.1.1.4")
unreachable = ("10.1.1.7", "10.1.1.8", "10.1.1.9")

print_ip_table(reachable, unreachable)