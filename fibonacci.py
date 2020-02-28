#!/usr/bin/env python
import time
import matplotlib.pyplot as plt
x_axis = []
y_axis = []
pid = 3346
with open("input_1.txt") as f:
  for x in f:
    n = int(x)
    x_axis.append(n)
    print('N: ' + str(n))
    time_start = time.time()
    def recur_fibo(n):
      if n <= 1:
        return n  
      else:
        return(recur_fibo(n-1) + recur_fibo(n-2))   
    print("Fibonacci sequence:")  
    for i in range(n):
      print(recur_fibo(i), end =" ")
    pid+=1
    print("\nPID = ",pid)
    time1 = ((time.time() - time_start)*100)
    y_axis.append(time1)
    print('time taken in seconds =' + str(time1))
print(x_axis)
print(y_axis)
plt.plot(x_axis,y_axis)
plt.xlabel('N')
plt.ylabel('Time(milliseconds)')
plt.title('Fibonacci Program')
plt.show()