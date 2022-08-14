import pandas as pd
import matplotlib.pyplot as plt

# plt.rcParams["figure.figsize"] = [7.50, 3.50]
# plt.rcParams["figure.autolayout"] = True

df = pd.DataFrame(
    dict(data=[14.93, 16.88, 17.31, 17.43, 17.74], data2=[1577.8, 2512.9, 4209.9, 5700.3, 7264.25]))
# print(df[0])


# fig, ax = plt.subplots()
barchart = plt.bar(df['data'], 20, color='red')

plt.twinx()
linechart = plt.plot(df['data2'],
                     color="blue",
                     marker="o")
# df['data'].plot(kind='bar', color='red')
# df['data2'].plot(kind='line', marker='*', color='black', ms=10)

plt.show()
