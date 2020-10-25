# -*- coding: utf-8 -*-
"""
Задание 15.1

Создать функцию get_ip_from_cfg, которая ожидает как аргумент имя файла,
в котором находится конфигурация устройства.

Функция должна обрабатывать конфигурацию и возвращать IP-адреса и маски,
которые настроены на интерфейсах, в виде списка кортежей:
* первый элемент кортежа - IP-адрес
* второй элемент кортежа - маска

Например (взяты произвольные адреса):
[('10.0.1.1', '255.255.255.0'), ('10.0.2.1', '255.255.255.0')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.


Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

"""

from pprint import pprint
import re

def get_ip_from_cfg(file):
    '''
    regex = re.compile(r"ip address (\S+) (\S+)")
    #1
    result = []
    with open(file) as f:
        for line in f:
            match = regex.search(line)
            if match:
                result.append(match.groups())
            
    #2
    with open(file) as f:
        result = [regex.search(line).groups() for line in f if regex.search(line)]
    '''
    #natenka
    regex = r"ip address (\S+) (\S+)"
    with open(file) as f:
        result = [match.groups() for match in re.finditer(regex, f.read())]
        
    
    return result

pprint(get_ip_from_cfg("config_r1.txt"))