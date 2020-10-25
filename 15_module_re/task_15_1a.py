# -*- coding: utf-8 -*-
"""
Задание 15.1a

Скопировать функцию get_ip_from_cfg из задания 15.1 и переделать ее таким образом, чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.

Например (взяты произвольные адреса):
{'FastEthernet0/1': ('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2': ('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

"""

from pprint import pprint
import re

def get_ip_from_cfg(file):
    '''
    result = {}
    regex_inf = re.compile(r"interface (\S+)")
    regex_ip = re.compile(r"ip address (\S+) (\S+)")
    inf = None
    
    with open(file) as f:
        for line in f:
            match_inf = regex_inf.search(line)
            match_ip = regex_ip.search(line)
            
            if match_inf:
                inf = match_inf[1]
            elif match_ip:
                result[inf] = (match_ip[1], match_ip[2])
    '''
    #natenka
    
    regex = re.compile(r"interface (\S+)\n( .*\n)* ip address (\S+) (\S+)")
    with open(file) as f:
        result = {match[1]: (match[3], match[4]) for match in regex.finditer(f.read())}
            
            
    return result


pprint(get_ip_from_cfg("config_r1.txt"))