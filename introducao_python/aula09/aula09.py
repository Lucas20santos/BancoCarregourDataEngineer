import os
os.system("clear")

arquivo = open('teste.txt', 'a')

arquivo.write("\n arquivo escrito terceira vez\n")
arquivo.close()

os.system("cat teste.txt")
