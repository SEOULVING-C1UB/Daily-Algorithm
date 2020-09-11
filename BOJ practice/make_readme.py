import os

input_data = open('README.md', 'r', encoding='UTF8')
input_data.readline()
pwd = os.getcwd()
for line in input_data.readlines():
    temp = line.split()
    name = pwd + '\\' + temp[1] + '\\'
    os.mkdir(name)
input_data.close()