import numpy as np
import matplotlib.pyplot as plt
from textwrap import wrap
import matplotlib.ticker as ticker

with open("/home/b01-206/Documents/mda/get/Lesson8_Graph/frequency.txt", "r") as file:
    freq = float(file.read().split(' ')[1])
    print("frequency =", freq)

data_arr = np.loadtxt("/home/b01-206/Documents/mda/get/Lesson8_Graph/data.txt", dtype=int)
data_arr = data_arr * 3.3 / 256
num_measures = len(data_arr)
time_arr = np.arange(num_measures)
time_arr = time_arr / freq
print("time_arr:", time_arr)

fig, axes = plt.subplots(figsize=(16, 10), dpi=400)

axes.axis([0, time_arr.max()+1, 0, 3.3])
axes.set_xlabel("Time, sec", fontsize=20)
axes.set_ylabel("Voltage, V", fontsize=20)

axes.xaxis.set_major_locator(ticker.MultipleLocator(5))
axes.xaxis.set_minor_locator(ticker.MultipleLocator(1))

axes.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
axes.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))

axes.minorticks_on()
axes.grid(which='major', color = 'k')
axes.grid(which='minor', color = 'lightgray')

axes.set_title("The process of charging a capacitor in RC-module", loc = "center", fontsize=30)

axes.plot(time_arr, data_arr, c='red', linewidth=1, label="V(t)")
axes.arrow(time_arr.max(), 3.3, 1, 0.1)
axes.scatter(time_arr[0:num_measures:20], data_arr[0:num_measures:20], marker='s', c='red', s=10)
axes.legend(shadow = False, loc = 'right', fontsize = 30)


fig.savefig("/home/b01-206/Documents/mda/get/Lesson8_Graph/graph.png")
plt.show()