# -*- coding: utf-8 -*-
"""
Задание 15.1b

Проверить работу функции get_ip_from_cfg из задания 15.1a на конфигурации config_r2.txt.

Обратите внимание, что на интерфейсе e0/1 назначены два IP-адреса:
interface Ethernet0/1
 ip address 10.255.2.2 255.255.255.0
 ip address 10.254.2.2 255.255.255.0 secondary

А в словаре, который возвращает функция get_ip_from_cfg, интерфейсу Ethernet0/1
соответствует только один из них (второй).

Скопировать функцию get_ip_from_cfg из задания 15.1a и переделать ее таким образом,
чтобы в значении словаря она возвращала список кортежей для каждого интерфейса.
Если на интерфейсе назначен только один адрес, в списке будет один кортеж.
Если же на интерфейсе настроены несколько IP-адресов, то в списке будет несколько кортежей.
Ключом остается имя интерфейса.

Проверьте функцию на конфигурации config_r2.txt и убедитесь, что интерфейсу
Ethernet0/1 соответствует список из двух кортежей.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

"""


from pprint import pprint
import re

def get_ip_from_cfg(file):
    '''
    #1
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
                if result.get(inf):
                    result[inf].append((match_ip[1], match_ip[2]))
                else:
                    result[inf] = [(match_ip[1], match_ip[2])]
    
    '''
    #2
    regex_ip = r"interface (\S+)\n( .*\n)* ip address (\S+) (\S+)"    
    regex_ipip = r"interface (\S+)\n( .*\n)* ip address (\S+) (\S+)\n ip address (\S+) (\S+)"    
    
    with open(file) as f:
        file_read = f.read()
   
        result = {match[1]: [(match[3], match[4])] for match in re.finditer(regex_ip, file_read)}
        result_ipip = {match[1]: [(match[3], match[4]), (match[5], match[6])] for match in re.finditer(regex_ipip, file_read)}
        
        result.update(result_ipip)
        
    return result


pprint(get_ip_from_cfg("config_r2.txt"))