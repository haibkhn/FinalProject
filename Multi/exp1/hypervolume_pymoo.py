# from pygmo import hypervolume
from pymoo.factory import get_performance_indicator
import numpy as np
import os

# os.chdir("exp1")
folder = "map1_moes/dimen"

'hypervolume' in dir()
allfile = os.listdir("exp1/" + folder)
# allfile.sort()
# print(allfile)

for file in allfile:
    f = open("exp1/" + folder + "/" + file, "r")

    hypervolumeArray = []
    hypervolumeList = []
    timeList = []
    flag = False

    while True:
        line = f.readline()
        tempstr = []
        while line.startswith("P") == True:
            flag = True
            mystr = line.split()
            for arr in mystr:
                if arr.replace('.', '', 1).isdigit():
                    tempstr.append(float(arr))
            hypervolumeArray.append(tempstr)
            line = f.readline()
            tempstr = []
        if hypervolumeArray != []:
            # print(hypervolumeArray)
            metric = get_performance_indicator(
                "hv", ref_point=np.array([120, 1.5, 2]))
            hypervolumeNumpyArray = np.array(hypervolumeArray)
            # print(hypervolumeNumpyArray)

            hv = metric.do(hypervolumeNumpyArray)
            hypervolumeList.append(hv)
            # print(hv)
            # hv = hypervolume(hypervolumeArray)
            # ref_point = [120, 1, 2]
            # ref_point = [85, 1, 2]
            # print(round(hv.compute(ref_point), 3))
        if (line.startswith("T") == True) and (flag == True):
            # print("Aaaaaaaaaa")
            mystr = line.split()
            # print(mystr[1])
            timeList.append(float(mystr[3]))
            hypervolumeArray = []
        if (line.startswith("-") == True):
            flag = False
            # print("Aaaaaaaaaa")
            hypervolumeArray = []
        if ("" == line):
            print("file finished")
            break

    # print(len(hypervolumeList))
    # print(len(timeList))
    avgHypervolume = (sum(hypervolumeList)/len(hypervolumeList))
    avgTime = (sum(timeList)/len(timeList))

    # print(f.name)
    file = open("exp1/result_map_2_moes.txt", 'a+')
    file.write(f.name+"\t"+str(round(avgHypervolume, 2)) +
               " " + str(round(avgTime, 2)) + "\n")
    file.close()
