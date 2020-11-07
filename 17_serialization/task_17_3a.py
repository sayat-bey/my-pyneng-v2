# -*- coding: utf-8 -*-
"""
Задание 17.3a

Создать функцию generate_topology_from_cdp, которая обрабатывает вывод команды show cdp neighbor из нескольких файлов и записывает итоговую топологию в один словарь.

Функция generate_topology_from_cdp должна быть создана с параметрами:
* list_of_files - список файлов из которых надо считать вывод команды sh cdp neighbor
* save_to_filename - имя файла в формате YAML, в который сохранится топология.
 * значение по умолчанию - None. По умолчанию, топология не сохраняется в файл
 * топология сохраняется только, если save_to_filename как аргумент указано имя файла

Функция должна возвращать словарь, который описывает соединения между устройствами, независимо от того сохраняется ли топология в файл.

Структура словаря должна быть такой:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}},
 'R5': {'Fa 0/1': {'R4': 'Fa 0/1'}},
 'R6': {'Fa 0/0': {'R4': 'Fa 0/2'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.

Проверить работу функции generate_topology_from_cdp на списке файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Проверить работу параметра save_to_filename и записать итоговый словарь в файл topology.yaml.

"""

import re
from pprint import pprint
import glob
import yaml

files = glob.glob("sh_cdp_n_*.txt")

def parse_sh_cdp_neighbors(cmd):
    result = {}
    hostname_regex = r"(\S+)>show"
    regex = r"(\S+) +(\S+ \S+) +\d+ .* +(\S+ \S+)"
    
    hostname_match = re.search(hostname_regex, cmd)
    if hostname_match:
        hostname = hostname_match[1]
        result[hostname] = {}
        
    for m in re.finditer(regex, cmd):
        neighbor = m[1]
        port = m[2]
        neighbor_port = m[3]
        result[hostname][port] = {neighbor: neighbor_port}
        
    return result
    
def generate_topology_from_cdp(list_of_files, save_to_filename=None):
    result = {}
    for file in list_of_files:
        with open(file) as f:
            result.update(parse_sh_cdp_neighbors(f.read()))
    
    if save_to_filename:
        with open(save_to_filename, "w") as fo:
            yaml.dump(result, fo, default_flow_style=False)
            
    return result

if __name__ == "__main__":
    f_list = glob.glob("sh_cdp_n_*")
    print(generate_topology_from_cdp(f_list, save_to_filename="topology.yaml"))
    
#pprint(generate_topology_from_cdp(files, "task_17_3a_output.yaml"))          