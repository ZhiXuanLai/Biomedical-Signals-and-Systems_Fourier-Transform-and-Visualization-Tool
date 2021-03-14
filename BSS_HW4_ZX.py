# -*- coding: utf-8 -*-
"""
2018/11/12 HW4
"""

import numpy as np
import matplotlib.pyplot as plt


T = 1
x = np.linspace(-2,2,2000)
y_A = np.zeros(x.shape)   # (x.size) is the number of elements  Different from (x.shape). x is 1D so both are ok here.
y_B = np.zeros(x.shape)
y_C = np.zeros(x.shape)
y_D = np.zeros(x.shape)
y_E = np.zeros(x.shape)
y_F = np.zeros(x.shape)
func_A = 1+x*0
func_B = 1-2*abs(x)/T
func_C = 0.5 + 0.5*np.cos(2*np.pi*x/T)
func_D = x/T + 0.5
func_E = np.cos(np.pi*x/2)
func_F = np.exp(-0.5*(x+T/2))

#plot the window function
def window_func(x, y, func, T) :  
    for i in range(x.size) :
        if x[i]>(-T/2) and x[i]<(T/2) :
            y[i] = func[i]
        else:
            y[i] = 0
    return y

y_A = window_func(x, y_A, func_A, T)
y_B = window_func(x, y_B, func_B, T)
y_C = window_func(x, y_C, func_C, T)
y_D = window_func(x, y_D, func_D, T)
y_E = window_func(x, y_E, func_E, T)
y_F = window_func(x, y_F, func_F, T)

# do FFT and plot
def func_FFT(x, y) :
    Ts = x[1]-x[0]  #time sampling interval
    Fs = 1/Ts       #sampling rate 取樣頻率
    n = x.size      #sample number
    t = n/Fs        #length of time
    k = np.arange(n)   #array size is the same as x    k=0, 1, 2, 3...
    freq = k/t      #two sides frequency range
    Y = np.fft.fft(y)     #compute FFT
    plt.plot(freq, Y)     #plot

# plot three figure for each
def func_plot(x, y) :
    plt.figure(figsize=(10,10))
    plt.subplot(3, 1, 1)        
    plt.plot(x, y)
    plt.xlabel("t") 
    plt.ylabel("y(t)") 
    plt.subplot(3, 1, 2)
    func_FFT(x, y)      
    plt.xlabel("f") 
    plt.ylabel("Y(f)") 
    plt.subplot(3, 1, 3) 
    func_FFT(x, y)      
    plt.xlim(-1,20)
    plt.xlabel("f") 
    plt.ylabel("Y(f)") 

func_plot(x, y_A)
plt.savefig(fname = "HW4_a.png", format = "png")
func_plot(x, y_B)
plt.savefig(fname = "HW4_b.png", format = "png")
func_plot(x, y_C)
plt.savefig(fname = "HW4_c.png", format = "png")
func_plot(x, y_D)
plt.savefig(fname = "HW4_d.png", format = "png")
func_plot(x, y_E)
plt.savefig(fname = "HW4_e.png", format = "png")
func_plot(x, y_F)
plt.savefig(fname = "HW4_f.png", format = "png")

