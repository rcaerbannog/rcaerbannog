import os, pathlib, pickle

filename = "pickle.txt"
my_list = ["Fred", 73, "Hello there!", 81.9876e-13]
with open(filename, 'wb') as pickle_file:
    pickle.dump(my_list, pickle_file)


recovered_list = None
with open(filename, 'rb') as unpickle_file:
    recovered_list = pickle.load(unpickle_file)
for i in recovered_list:
    print (i)
