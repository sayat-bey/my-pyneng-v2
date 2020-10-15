# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

import subprocess

def ping_ip_addresses(ip_list):
    
    available = []
    unavailable = []
    
    for ip in ip_list:
        result = subprocess.run(["ping", "-c", "3", ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if result.returncode == 0:
            available.append(ip)
            
        else:
            unavailable.append(ip)
    
    return available, unavailable
    

ip_list = ["1.1.1", "8.8.8.8", "8.8.4.4", "8.8.7.1"]
