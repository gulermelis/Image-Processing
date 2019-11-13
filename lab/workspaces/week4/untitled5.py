# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 16:24:47 2019

@author: Melis GULER
"""

import numpy as np
import matplotlib.pyplot as plt


data_path ="C:/Users/Melis GULER/.jupyter/lab/workspaces/week4/"
train_data = np.loadtxt(data_path + "mnist_train.csv", delimiter=",") 
test_data = np.loadtxt(data_path + "mnist_test.csv", delimiter=",")



image_size = 28 # width and length
no_of_different_labels = 10 #  i.e. 0, 1, 2, 3, ..., 9
image_pixels = image_size * image_size #28*28+1=785 piksel

print(train_data.ndim,train_data.shape )      #(2 (60000,785))
print(test_data[:10])

print(train_data[10,50]) #10. satır 50. elemanı
print(train_data[10,0]) #10. satır 0. elemanı : eleman=3
im_3=train_data[10,:] #10. satırdaki elemanları komple im_3'e atar #785
print(im_3.shape)

im_4=im_3[1:] 
print(im_4.shape) #784

im_5=im_4.reshape(28,28)
plt.imshow(im_5,cmap='gray')
plt.show()

#rakamlardan kaçar tane olduğunu bulan fonksiyon:
m,n=train_data.shape
m,n #sonuç=(60000,785)

def my_count(k=0):
    s=0
    for i in range (m):
        if(train_data[i,0]==k):
            s=s+1
    return s #kaç tane k değeri olduğunu bastırır.
for i in range(10):
    c=my_count(i)
    print(i," ",c) # 0-10 sayılarından kaçar tane olduğunu yazdırır.
    
    import math
def my_pdf_1(x,mu=0.0,sigma=1.0):
    x=float(x-mu)/sigma
    return math.exp(-x*x/2.0)/math.sqrt(2.0*math.pi)/sigma

#değeri 0 olan resimlerin sol üstteki pixelin ortalama ve standart sapmasını bulan fonksiyon:
s,t,k=0,0,0
l=350 #lokasyon
for i in range (m):
    if(train_data[i,0]==k):
        s=s+1 #kaç tane var
        t=t+train_data[i,l+1] #instensity değerleri
mean_1=t/s #ortalama
s,t=0,0
for i in range (m):
    if(train_data[i,0]==k):
        s=s+1 #kaç tane var
        diff_1=train_data[i,l+1]-mean_1
        t=t+diff_1*diff_1
std_1=np.sqrt(t/(s-1))
print(mean_1,std_1)

#yukarıdaki kodları fonksiyon haline getirdik: 
def get_my_mean_and_std(k=0,l=0):
    s=0
    t=0
    for i in range(m):
        if(train_data[i,0]==k):
            s=s+1
            t=t+train_data[i,l+1]
    mean_1=t/s

    s,t=0,0
    for i in range(m):
        if(train_data[i,0]==k):
            s=s+1
            diff_1=train_data[i,l+1]-mean_1
            t=t+diff_1*diff_1
    std_1=np.sqrt(t/(s-1))
    return mean_1,std_1


im_1=plt.imread('test_1.jpg')
plt.imshow(im_1)
plt.show()
test_value=im_1[0,0,0]

m_1,std_1=get_my_mean_and_std(2,100)
my_pdf_1(test_value,m_1,std_1)
