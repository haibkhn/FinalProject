import matplotlib.pyplot as plt
import numpy as np

# plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

HV = np.array([18.1, 20.22, 19.35, 19.93, 17.72, 15.61, 16.76, 16.4])
time = np.array([4368.9, 4848.7, 5172.75, 5508.75,
                5790.85, 6106.25, 6592.8, 7225.1])
title = ["8", "9", "10", "11", "12", "13", "14", "15"]
ax1 = plt.subplot()
l1 = ax1.bar(title, HV, color='green')
ax2 = ax1.twinx()
l2 = ax2.plot(time, color='red')
# ax1.setylim
ax1.set_ylabel("HV values")
ax2.set_ylabel("Times (ms)")
ax2.set_ylim(top=8000)
ax1.set_ylim(bottom=15, top=22)
ax1.set_xlabel("Number of segments")
# plt.legend([l1, l2], ["HV", "time"])

plt.show()
