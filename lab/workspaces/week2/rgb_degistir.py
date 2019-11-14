
import os
print(os.getcwd())   #dizini bul
print(os.listdir()) 

import numpy as np
my_list_1=np.array([3,3,3,3,3,3]) #ndarray
print(my_list_1+1)
def np_list_deneme(my_array=np.array([3,3,3,3,3,3])):
    return my_array-10

print(np_list_deneme())


import matplotlib.pyplot as plt

image=plt.imread('dubai.jpg')
plt.imshow(image)
plt.show()

m,n,p=image.shape
new_img=np.zeros((m,n,3),dtype=int)
for i in range(image.shape[0]):       #shape olduğu için 'range' eklenmeli
    for j in range(image.shape[1]):
        #pixel pixel gezip her pixel'i im_2 ye atarken işlem yapılır
        new_img[i,j,0]=image[i,j,0]+100 #red
        new_img[i,j,1]=image[i,j,1]     #g
        new_img[i,j,2]=image[i,j,2]     #b

plt.imshow(new_img)
plt.show()

def red_degistir(img,s):  #verilen s degeri kadar rgb red degerini azalt
    m,n,p=image.shape
    img1=np.zeros((m,n,3),dtype=int)
    m,n,p=img1.shape
    for m in range(image.shape[0]): 
        for n in range(image.shape[1]):
            img1[m,n,0]=image[m,n,0]+s
            img1[m,n,1]=image[m,n,0]
            img1[m,n,2]=image[m,n,0]
            
    return img1

im_red=red_degistir(image,100)  
plt.imshow(im_red)
plt.show()