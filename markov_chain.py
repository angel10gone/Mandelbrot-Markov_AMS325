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
    #makes all entries in each row sum to one
    P /= P.sum(1, keepdims=True)
    #computes eigenvector for largest eigenvalue in PT
    val, vect = np.linalg.eig(P.T)
    vect = vect[:,np.argmax(val)]
    #Rescales entries so sum is equal to one
    p_stationary = vect/vect.sum()
    diff = 0
    #creates array to store difference of norms
    y = []
    #computes norm of p-p_stationary
    for i in range(N):
        #calculates p after transitioning N times
        p = np.dot(P.T, p)
        diff = np.linalg.norm(np.subtract(p, p_stationary))
        #stores norms in y array
        y.append(diff)
    #plot norms against i
    x = np.linspace(0, N, N)
    plt.plot(x, y)

#test markov_chain function for different values of n and N
markov_chain(n=5, N=50)
markov_chain(n=5, N=55)
markov_chain(n=5, N=60)
