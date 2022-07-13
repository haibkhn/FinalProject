import matplotlib.pyplot as plt
import numpy as np

# plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

HV = np.array([9.22, 16.0, 17.2, 17.61, 17.93, 17.92])
time = np.array([2108.15, 2537.4, 6229.9, 7662.0, 16914.65, 31722.05])
title = ["(50;5)", "(50;10)", "(100;20)", "(100;30)", "(150;50)", "(200;80)"]
ax1 = plt.subplot()
l1 = ax1.bar(title, HV, color='green')
ax2 = ax1.twinx()
l2 = ax2.plot(time, color='red')
# ax1.setylim
ax1.set_ylabel("HV values")
ax2.set_ylabel("Times (ms)")
ax2.set_ylim(top=33000)
ax1.set_ylim(bottom=7, top=20)
ax1.set_xlabel("(Number of Children; Number of Elite)")
# plt.legend([l1, l2], ["HV", "time"])

plt.show()
