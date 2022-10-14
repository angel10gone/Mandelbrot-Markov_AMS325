# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 17:17:24 2022

@author: Angel
"""
import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(n, N_max, threshold):
    """
        
    Parameters
    ----------
    n : TYPE: int
        DESCRIPTION: size of Mandelbrot set.
    N_max : TYPE: int
           DESCRIPTION: number of Mandelbrot iterations.
    threshold : TYPE: float
                DESCRIPTION: value to indicate what points are in the Mandelbrot set.
                
    Returns
    -------
    mask: 2-D array indicating whether point is in Mandelbrot set
    """
    #creates an array of range of x values in set
    x = np.linspace(-2, 1, n)
    #creates an array of the range of y values in the set
    y = np.linspace(-1.5, 1.5, n)
    #creates nxn grid with x, y values
    xc, yc = np.meshgrid(x, y, indexing='ij')
    #creates grid with corresponding complex values
    c = xc + 1j * yc
    
    #find Mandelbrot set for N_max iterations
    z = 0
    for j in range(N_max):
        z = z**2 + c
    
    #creates array indicating if points are in the set
    mask = (abs(z) < threshold)
    return mask

#call and test function
mask = mandelbrot(n=500, N_max=50, threshold=50)

#plots and saves function
plt.imshow(mask.T, extent=[-2, 1, -1.5, 1.5])
plt.gray()
plt.savefig('mandelbrot.png')