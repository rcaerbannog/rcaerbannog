import os

filename = "Text Files\\r.txt"
my_file = open(filename, 'r')
lines = my_file.readlines()
for line in lines:
    print(line)
my_file.close()
