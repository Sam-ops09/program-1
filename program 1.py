# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 21:22:56 2020

@author: Samanyu B Rao
"""

''' object oriented programming'''

class A:
    x=5
    y=10
    def myfun(self):
        print('I am a function of class A')
        print(self.x+self.y+20)
        self.c=20

    def myfun4(self,a,b):
        print(self.c)
        print(a+b)
        return a-b

class B(A):
    def yourfun(self):
        print('I am function of class ')


import time
print('sleep')
time.sleep(3)
print('woke up')


"""
Numpy - Data computation,
numerical analysis, mathematical coumputing

matlotlib - data visualization,
data graphical representation

Pandas - Data exploring, Handling and fetching

scikit-learn - data prediction, regression,
machine learning algorithom
"""
import numpy
data=numpy.random.randint(5,50,(10,5))
c=['Temperature', 'pressure', 'gas', 'humidity', 'light']
import pandas
dates=pandas.date_range('20170908',periods=10)
df=pandas.DataFrame(data,index=dates,columns=c)
