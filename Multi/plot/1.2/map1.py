import matplotlib.pyplot as plt
import numpy as np

# plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

HV = np.array([31.56, 111.26, 130.37, 132.3, 135.21, 135.35])
time = np.array([1543.95, 1643.1, 3363.7, 4121.5, 8406.35, 14741.15])
title = ["(50;5)", "(50;10)", "(100;20)", "(100;30)", "(150;50)", "(200;80)"]
ax1 = plt.subplot()
l1 = ax1.bar(title, HV, color='green')
ax2 = ax1.twinx()
l2 = ax2.plot(time, color='red')
# ax1.setylim
ax1.set_ylabel("HV values")
ax2.set_ylabel("Times (ms)")
ax2.set_ylim(top=16000)
ax1.set_ylim(bottom=0, top=150)
ax1.set_xlabel("(Number of Children; Number of Elite)")
# plt.legend([l1, l2], ["HV", "time"])

plt.show()
