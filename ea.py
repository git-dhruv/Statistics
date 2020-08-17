'''
@author: Dhruv Parikh
Date: August 2020
Purpose: Code illustrates the number 
'''
import matplotlib.pyplot as plt
import os
import csv
import numpy as np
from matplotlib.widgets import Slider
import stats as s
os.chdir('C:\\Users\\Dhruv\\Desktop')
N = 10

def change_N(val):
    N = int(s_N.val)
    global m_avg
    global e_avg
    global ls

    m_avg.remove()
    e_avg.remove()
    init.update_N(N)
    ma = init.moving_average()
    ea = init.exp_average()
    if N>=10:
        ls.remove()
        coeffs = init.least_squares(int(N/10),t)
        ls, = ax.plot(t,coeffs,label = 'Least Sqr',color='g')
    
    m_avg, = ax.plot(t[N-2:-1],ma,label = 'Moving Average',color='k')
    e_avg, = ax.plot(t[N-1:-1],ea,label = 'Expon Average',color='r')


fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)

axcolor = 'lightgoldenrodyellow'
ax_N = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
s_N = Slider(ax_N,'N',2,499,valinit=1,valstep=1)

with open('yahooo.csv','r') as f:
    x = [float(row[0])/1000 for row in csv.reader(f)]

init = s.Statistics(x,N)
ma = init.moving_average()
ea = init.exp_average()

t = [i/100 for i in range(len(x))]

coeffs = init.least_squares(5,t)

ax.plot(t,x,label='orignal')
global m_avg
global e_avg
global ls
m_avg, = ax.plot(t[N-2:-1],ma,label = 'Moving Average',color='k')
e_avg, = ax.plot(t[N-1:-1],ea,label = 'Expon Average',color='r')
ls,  = ax.plot(t,coeffs,color='g')
ax.legend(loc='upper right')
s_N.on_changed(change_N)
plt.show()
        

'''
    def least_squares(self,deg):
        A = np.zeros([deg+1,deg+1])
        C = np.zeros([deg+1])
        t = [i for i in range(len(self.x))]
        for i in range(deg+1):
            for j in range(deg+1):
                A[i][j] = self.sum_power(self.x,i+j)
            temp = np.power(self.x,i)
            C[i] = np.sum(np.multiply(temp,t))
        coeffs = np.dot(np.linalg.inv(A),C)
        temp = []
        print(A)
        print(C)
        print(coeffs)
        for x in t:
            ans = [x**i for i in range(deg+1)]
            temp.append(np.dot(ans,coeffs))
        return temp
    def sum_power(self,x,power):
        squares = [x[i]**power for i in range(len(x))]
        return sum(squares)

'''
    
