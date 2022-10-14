# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 14:10:23 2022

@author: Angel
"""
import numpy as np
import matplotlib.pyplot as plt


def markov_chain(n, N):
    """
    
    Parameters
    ----------
    n : TYPE:int
        DESCRIPTION: number determining the size of the vector for the Markov chain and the distribution on n states,
    N : TYPE: int
        DESCRIPTION: number of itereations in Markov chain.

    Returns
    -------
    None.

    """
    #creates n-vector of random non-negative entries
    p = np.random.rand(n)
    #makes all entries sum to one
    p /= p.sum()
    #creates nxn P matrix of random wavlues
    P = np.random.rand(n,n)
    P /= P.sum()
    #computes transiton for N
    for j in range(N):
        p = np.dot(P.T, p)
    #computes eigenvector for largest eigenvalue in PT
    val, vect = np.linalg.eig(P.T)
    vect = vect[:,np.argmax(val)]
    #Rescales entries so sum is equal to one
    p_stationary = vect/vect.sum()
    diff = 0
    #computes norm of p-p_stationary
    for i in range(N):
        diff = np.linalg.norm(np.subtract(p, p_stationary))
    #plot norms against i
    x = np.linspace(0, N, N)
    y = np.linspace(0, diff, N)
    plt.plot(x, y)
    #create something to check if diff diminishes as iterations increase
    print(diff)
 
#test markov_chain function for different values of n and N
markov_chain(n=5, N=50)
markov_chain(n=10, N=50)
markov_chain(n=5, N=55)
markov_chain(n=20, N=55)
markov_chain(n=5, N=70)

