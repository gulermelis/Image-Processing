# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 14:38:40 2019

@author: Melis GULER
"""
my_list_1=[2,4,3,40,5,6,3,3,2,1]
def my_fun_1(my_list_1=[2,4,3,40,5,6,3,3,2,1]):
    t=0
    s=0
    for i in my_list_1:
        s=s+1
        t=t+i
    ortalama=t/s
    
    t=0
    s=0
    for i in my_list_1:
        s=s+1
        t=t+(i-ortalama)*(i-ortalama)
    varyans=t/(s-1)
    
    return ortalama, varyans
print(my_fun_1())

import matplotlib.pyplot as plt
import numpy as np
im_1=plt.imread('chicago.jpg')
#im_1.shape #en,boy,color
print(im_1.ndim,im_1.shape)

#histogramı bulan fonksiyon:
def my_fun_2(im_1=plt.imread('chicago.jpg')):
    m,n,p=im_1.shape
    my_histogram={}
    for i in range (m):
        for j in range (n):
            if im_1[i,j,0] in my_histogram.keys():
                my_histogram[im_1[i,j,0]]=my_histogram[im_1[i,j,0]]+1
            else:
                my_histogram[im_1[i,j,0]]=1
    return my_histogram

def my_fun_3(my_histogram=my_fun_2()):
    x=[] #soldaki değerler
    y=[] #sağdaki değerler
    for key in my_histogram.keys():
        x.append(key)
        y.append(my_histogram[key])
    return x,y

x,y=my_fun_3()
plt.bar(x,y) #grafiğe aktarma
plt.show()
print(my_fun_3())