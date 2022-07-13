import matplotlib.pyplot as plt
import numpy as np

# plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

HV = np.array([16.45, 16.64, 16.85, 17.57, 18.35])
time = np.array([3700.15, 7984.95, 15119.3, 22212.0, 29334.65])
title = ["20", "50", "100", "150", "200"]
ax1 = plt.subplot()
l1 = ax1.bar(title, HV, color='green')
ax2 = ax1.twinx()
l2 = ax2.plot(time, color='red')
# ax1.setylim
ax1.set_ylabel("HV values")
ax2.set_ylabel("Times (ms)")
ax2.set_ylim(top=30000)
ax1.set_ylim(bottom=14, top=20)
ax1.set_xlabel("Number of Generation")
# plt.legend([l1, l2], ["HV", "time"])

plt.show()
