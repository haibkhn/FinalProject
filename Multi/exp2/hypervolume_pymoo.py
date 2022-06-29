# from pygmo import hypervolume
from pymoo.factory import get_performance_indicator
import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# os.chdir("exp1")
map = "map5b"
'hypervolume' in dir()
allfile = os.listdir("exp2/"+map)
# allfile.sort()
print(allfile)
box = []

for file in allfile:
    f = open("exp2/"+map+"/" + file, "r")

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
                "hv", ref_point=np.array([250, 1.5, 2]))
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
    file = open("exp2/result_"+map+".txt", 'a+')
    file.write(f.name+"\t"+str(round(avgHypervolume, 2)) +
               " " + str(round(avgTime, 2)) + "\n")
    file.close()
    box.append(hypervolumeList)

# print(box)
df = pd.DataFrame()
df["V-MOES"] = box[0]
df["MOES"] = box[1]
df["MOPSO"] = box[2]
df["NSGA-II"] = box[3]
# df["HMOPSO-ES"] = box[3]

df.boxplot()
for i, d in enumerate(df):
    y = df[d]
    x = np.random.normal(i + 1, 0.04, len(y))
    plt.scatter(x, y)
plt.title(map)
plt.savefig("exp2/"+map+".pdf", format="pdf", bbox_inches="tight")

plt.show()
# print(df)
# df = pd.DataFrame(box, columns=["MOES", "MOPSO", "NSGA-II", "HMOPSO-ES"])
# sns.set(rc={'figure.figsize': (10, 7)})

# sns.boxplot(x="variable", y="value", data=pd.melt(df))

# fig = plt.figure(figsize=(10, 7))

# Creating plot
# plt.boxplot(box)

# show plot
# plt.show()
