'''
@author: Dhruv Parikh
Date: August 2020
Production and Operations Management
Time series data analytical tool developed to perform various statistical operations
'''

'''
Use Case displayed in the driver function at the end

====Simple Use Case====
import stats as s

intialize = s.Statistics(x,N)
pts = initialize.moving_average()
plt.plot(pts)
plt.show()
'''

'''
___       __
|  \ |_| |__|  |  |  \  /
|__/ | | |  \  |__|   \/

The author takes no guarentee for the performance of algorithms, these are just the tools
to aid in education
'''
import numpy as np
import matplotlib.pyplot as plt
class Statistics():
    def __init__(self,x,N):
        print('Stats tool made by:')
        print('___       __')
        print('|  \ |_| |__|  |  |  \  /')
        print('|__/ | | |  \  |__|   \/')
        
        self.x = x
        self.N = N
        self.ma = 0
    def moving_average(self):
        x = self.x
        N = self.N
        self.ma = [sum(x[i:i+N])/N for i in range(len(x)-N+1)]
        return self.ma

    def exp_average(self):
        if self.ma:
            EMA = self.ma[0]
        else:
            moving_average(self)
            EMA = self.ma[0]
        N = self.N
        multiplier = 2/(N+1)
        self.ea = []
        for i in self.x[N:]:
            self.ea.append((i-EMA)*multiplier + EMA)
            EMA = self.ea[-1]
            
        return self.ea
    
    def least_squares(self,deg,t):
        A = np.zeros([deg+1,deg+1])
        C = np.zeros([deg+1])
        for i in range(deg+1):
            for j in range(deg+1):
                A[i][j] = self.sum_power(t,i+j)
            temp = np.power(t,i)
            C[i] = np.sum(np.multiply(temp,self.x))
        coeffs = np.dot(np.linalg.inv(A),C)
        temp = []
        for x in t:
            ans = [x**i for i in range(deg+1)]
            temp.append(np.dot(ans,coeffs))
        return temp
    def sum_power(self,x,power):
        squares = [x[i]**power for i in range(len(x))]
        return sum(squares)

    def update_N(self,N):
        self.N  = N
        _ = self.moving_average()
        _ = self.exp_average()
        
if __name__ == '__main__':
    x = [(i)**2 for i in range(1000)]
    t = [i/1000 for i in range(len(x))]
    init = Statistics(x,1)
    plt.plot(t,init.least_squares(2,t))
    plt.show()
