# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 08:26:09 2018

@author: Rashmi
"""

import matplotlib.pyplot as plt
import csv
from decimal import *

x = []
y = []


with open('C:/Users/Rashmi/Desktop/Book1.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(float(row[1])) 
       

plt.plot(x,y, label='Networks')
plt.xlabel('Years')
plt.ylabel('probability of occurances')
plt.title('Evolution of "Networks"')
plt.legend()
plt.show()


