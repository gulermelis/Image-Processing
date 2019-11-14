


import os
print(os.getcwd())
print(os.listdir())

import numpy as np
import matplotlib.pyplot  as plt

img=plt.imread("dubai.jpg")

def boyutlandir(imm):
    #gönderilen mxn lik resmi m/2 x n/2 lik yapan fonksiyon
    m,n,p=imm.shape
    new_m=int(m/2)
    new_n=int(n/2)
    im_5=np.zeros((new_m,new_n),dtype=float)
    for m in range(new_m): 
        for n in range(new_n):
            s=(imm[m*2,n*2,0]+imm[m*2,n*2,1]+imm[m*2,n*2,2])/3
            im_5[m,n]=float(s)
    return im_5

plt.imshow(img)
plt.show()
img_kucuk=boyutlandir(img) 
plt.imshow(img_kucuk)
plt.show()  #resim boyutu kuculdu ama resmin netliği bozuldu


def boyut_Degis11(img):
    m,n,p=img.shape
    new_m=int(m/2)
    new_n=int(n/2)
    im_8=np.zeros((new_m,new_n,3),dtype=int)
    for m in range(new_m): 
        for n in range(new_n):
            im_8[m,n,0]=int(img[m*2,n*2,0])
            im_8[m,n,1]=int(img[m*2,n*2,1])
            im_8[m,n,2]=int(img[m*2,n*2,2])
    return im_8

plt.imshow(img)
plt.show()
img_yeni= boyut_Degis11(img) #resim boyutu bozulmalar olmadan kuculdu 
plt.imshow(img_yeni)
plt.show()

#plt.imsave("test.png",img_yeni,cmap="gray") bu satır hata veriyor??


img2= boyut_Degis11(img_yeni)
plt.imshow(img2)
plt.show()
img3= boyut_Degis11(img2)
plt.imshow(img3)
plt.show()