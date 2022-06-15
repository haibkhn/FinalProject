# from pygmo import hypervolume
from pymoo.factory import get_performance_indicator
import numpy as np
import os

# os.chdir("exp1")
map = "map5b"

'hypervolume' in dir()
allfile = os.listdir("exp2/"+map)
# allfile.sort()
# print(allfile)
hypervolumeArray = []

for file in allfile:
    f = open("exp2/"+map+"/" + file, "r")

    while True:
        line = f.readline()
        tempstr = []
        while line.startswith("P") == True:
            mystr = line.split()
            for arr in mystr:
                if arr.replace('.', '', 1).isdigit():
                    tempstr.append(float(arr))
            hypervolumeArray.append(tempstr)
            line = f.readline()
            tempstr = []
        if ("" == line):
            # print("file finished")
            break

hypervolumeNumpyArray = np.array(hypervolumeArray)
x, y, z = hypervolumeNumpyArray.max(axis=0)
print(x, y, z)
