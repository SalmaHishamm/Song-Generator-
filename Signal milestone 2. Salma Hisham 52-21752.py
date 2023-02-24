# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt 
import sounddevice as sd
from scipy.fftpack import fft

t=np.linspace(0,3,12*1024)    #time
ti =np.array([0,0.42,0.84,1.26,1.7,2.12,2.54,2.96])   #ti the starting point of each beat
Ti=np.array([0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4])   #Ti the duration of beat
f=np.array([329.63,293.66,261.63,293.66,349.23,329.63,293.66,261.63]) #freq array 

def unit_step_shifted (x,y): #method generates shifted unit step func
    x1=np.reshape([(t-(x+y))>=0],np.shape(t))
    return (x1)  

def unit_step (m):  #method generates unit step func
    x1=np.reshape([(t-m)>=0],np.shape(t))
    return (x1)



p=0

for i in range(8): #for loop to generate the sum of beats 
    b=(unit_step(ti[i])+(unit_step_shifted (ti[i],Ti[i]))*-1)*np.sin(2*np.pi*f[i]*t)
    p=p+b
    #print(p)


 
#plt.plot(t,p)  #plotting 
#sd.play(p,3*1024) #sound production



N = 3*1024
f = np. linspace(0,512 ,int(N/2))  #sampling

x_f = fft(p)
x_f = 2/N * np.abs(x_f [0:np.int(N/2)]) #getting the original song in freq domain


f𝑛1= np.random.randint(0, 512,1)  #generating two random noises
f𝑛2= np.random.randint(0, 512,1)

𝑛oise1 = np.sin (2*f𝑛1*np.pi*t)
noise2 =np.sin( 2*f𝑛2*np.pi*t)

Noised=p+noise1+noise2  #adding the noise to the original song

x_f2 = fft(Noised)
x_f2 = 2/N * np.abs(x_f2 [0:np.int(N/2)]) #getting the noised song in freq domain

#plt.plot(t,Noised)  
#plt.plot(f,x_f)
#plt.plot(f,x_f2)

#sd.play(out,3*1024) #sound production

temp=0
n=0
max1=0
max_number1=max(x_f2)

for n in range (len(x_f2)):     #loop1=get the first max (noise 1) using freq domain 
    if (x_f2[n]==max_number1):
        max1=n
        temp=x_f2[n]
        x_f2[n]=0
        break
    
m=0
max2=0
max_number2=max(x_f2)

for m in range (len(x_f2)):    #loop2=get the second max (noise 2) using freq domain
    if (x_f2[m]==max_number2):
        max2=m
        break

x_f2[n]=temp  
  
f1= round(f[n])   #round up the noise beat
f2 = round(f[m])   #round up the noise beat


xfilter = Noised -np.sin(2*f1*np.pi*t)-np.sin(2*f2*np.pi*t) #getting the filtered song(without noise)

x_f3 = fft(xfilter)
x_f3 = 2/N * np.abs(x_f3 [0:np.int(N/2)]) #getting the filtered song in freq domain



sd.play(xfilter,3*1024)  #playing the filtered song


plt.subplot(3,2,1)
plt.plot(t,p)    #plotting time domain of original
plt.subplot(3,2,2) 
plt.plot(f,x_f)  #plotting freq domain of original
plt.subplot(3,2,3)
plt.plot(t,Noised) #plotting time domain of noised
plt.subplot(3,2,4)
plt.plot(f,x_f2)  #plotting freq domain of noised
plt.subplot(3,2,5)
plt.plot(t,xfilter) #plotting time domain of filtered
plt.subplot(3,2,6)
plt.plot(f,x_f3)  #plotting freq domain of filtered




#print(f1)
#print(f2)
#print(fn1)
#print(fn2)
    
    
    
    