

import os
print(os.getcwd())   #dizini bul
print(os.listdir())   #dizindeki dosyaları bul
import numpy as np
import matplotlib.pyplot as plt

im_1=plt.imread('chicago.jpg')
print(im_1.shape)  #boyutlar.. yukseklik,genişlik,RGB
print(im_1.ndim)  #kac boyutlu 3, siyah beyaz resimler 2 boyutludur
m,n,p=im_1.shape
plt.imshow(im_1)
plt.show()
im_2=np.zeros((m,n), dtype=float)
for i in range(m):
    for j in range(n):
        s=(im_1[i,j,0]+im_1[i,j,1]+im_1[i,j,2])/3
        im_2[i,j]=s
        
plt.imshow(im_2, cmap="gray")  # siyah beyaz resim
plt.show()
plt.imsave("siyahbeyazchicago.jpg",im_2,cmap="gray") #kaydedilir

im_3=np.zeros((n,m),dtype=float) # resim doksan derece dondurulecek
for i in range(m):
    for j in range(n):
        s=(im_1[i,j,0]+im_1[i,j,1]+im_1[i,j,2])/3
        im_3[j,i]=s
        
plt.imshow(im_3, cmap="gray") #siyahbeyaz olarak dondurur
plt.show()
plt.imsave("doksanderece.jpg",im_3,cmap="gray") #kaydedilir
plt.imshow(im_3) #renkli dondurur
plt.show()