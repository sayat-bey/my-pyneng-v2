# -*- coding: utf-8 -*-
"""
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

from sys import argv


file_argv = argv[1]
file_output_argv = argv[2]

file = open(file_argv)
file_output = open(file_output_argv, "w")
ignore = ["duplex", "alias", "Current configuration"]

for line in file:
    ignore_state = False
    
    for i in ignore:
        if i in line:
            ignore_state = True
    
    if not ignore_state:
        file_output.write(line)

file.close()
file_output.close()