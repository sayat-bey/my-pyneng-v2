# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""



from pprint import pprint

def get_int_vlan_map(config_filename):

    access = {}
    trunk = {}
    
    with open(config_filename) as file: 
        for line in file:
            if line.startswith("interface "):
                inf = line.split()[-1]
            elif "switchport mode access" in line:
                access[inf] = 1
            elif line.startswith(" switchport access vlan"):
                access[inf] = int(line.split()[-1])
                
            elif line.startswith(" switchport trunk allowed vlan"):
                vlans = line.split()[-1].split(",")
                trunk[inf] = [int(i) for i in vlans]
        
    return access, trunk
    
pprint(get_int_vlan_map("config_sw2.txt"))
