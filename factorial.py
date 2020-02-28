#!/usr/bin/env python
import math
import time
from datetime import datetime
import matplotlib.pyplot as plt
pid = 2345
x_axis = []
y_axis = []
with open("input.txt") as f:
  for x in f:
    n = int(x)
    x_axis.append(n)
    time_start = time.time()
    print('N: ' + str(n))
    fact = math.factorial(n)
    print('result = ' + str(fact))
    pid+= 1
    print('Process ID = ' + str(pid))
    time1 = ((time.time() - time_start)*100)
    y_axis.append(time1)
    print('time taken in seconds =' + str(time1))
print(x_axis)
print(y_axis)
plt.plot(x_axis,y_axis)
plt.xlabel('N')
plt.ylabel('Time(milliseconds)')
plt.title('Factorial Program')
plt.show()