import matplotlib.pyplot as plt
import os
import csv
import numpy as np
from matplotlib.widgets import Slider

os.chdir('C:\\Users\\Dhruv\\Desktop')
N = 10

global x
global t

def moving_average(x,N):
    return [sum(x[i:i+N])/N for i in range(len(x)-N+1)]
def change_N(val):
    global m_avg
    global x
    global t
    m_avg.remove()
    N = int(s_N.val)
    m_avg, = ax.plot(t[N-2:-1],moving_average(x,N),label = str(N),color='r')
    
    
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)

axcolor = 'lightgoldenrodyellow'
ax_N = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
s_N = Slider(ax_N,'N',2,499,valinit=1,valstep=1)

with open('yahooo.csv','r') as f:
    x = [float(row[0]) for row in csv.reader(f)]
    
t = [i for i in range(len(x))]

ax.plot(t,x,label='orignal')
#ax.plot(t[N-2:-1],moving_average(x,N),label = str(N))
#N = N-5
N = 2
global m_avg
m_avg, = ax.plot(t[N-2:-1],moving_average(x,N),label = str(N))
ax.legend(loc='upper left')

s_N.on_changed(change_N)
plt.show()
        
        
    
