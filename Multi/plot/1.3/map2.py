import matplotlib.pyplot as plt
import numpy as np

# plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

HV = np.array([13.42, 14.2, 14.08, 14.02, 13.6, 13.66, 13.01, 13.04])
time = np.array([5292.05, 5767.1, 6303.6, 6566.7,
                7116.4, 7804.45, 8245.05, 9005.2])
title = ["8", "9", "10", "11", "12", "13", "14", "15"]
ax1 = plt.subplot()
l1 = ax1.bar(title, HV, color='green')
ax2 = ax1.twinx()
l2 = ax2.plot(time, color='red')
# ax1.setylim
ax1.set_ylabel("HV values")
ax2.set_ylabel("Times (ms)")
ax2.set_ylim(top=10000)
ax1.set_ylim(bottom=12, top=15)
ax1.set_xlabel("Number of segments")
# plt.legend([l1, l2], ["HV", "time"])

plt.show()
