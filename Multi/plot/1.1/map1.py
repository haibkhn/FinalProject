import matplotlib.pyplot as plt
import numpy as np

# plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

HV = np.array([14.93, 16.88, 17.31, 17.43, 17.74])
time = np.array([1577.8, 2512.9, 4209.9, 5700.3, 7264.25])
title = ["20", "50", "100", "150", "200"]
ax1 = plt.subplot()
l1 = ax1.bar(title, HV, color='green')
ax2 = ax1.twinx()
l2 = ax2.plot(time, color='red')
# ax1.setylim
ax1.set_ylabel("HV values")
ax2.set_ylabel("Times (ms)")
ax2.set_ylim(top=8000)
ax1.set_ylim(bottom=14, top=18)
ax1.set_xlabel("Number of Generation")
# plt.legend([l1, l2], ["HV", "time"])

plt.show()
