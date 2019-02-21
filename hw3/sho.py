import numpy as np
import matplotlib.pyplot as plt

def sho_euler_explicit(x0, v0, tmax, h):
    N = int(tmax/h) + 1
    
    out = np.zeros((2,N))
    H = np.array([[1,h],[-h,1]])
    
    out[0,0] = x0
    out[0,1] = v0
    
    for i in range(1,N):
        out[:,i] = np.dot(H, out[:,i-1])
    
    return out;

def sho_analytic(x0, v0, tmax, h):
    
    N = int(tmax/h)+1
    
    t = np.linspace(0,tmax,N)
    out = np.zeros((2,N))
    
    out[0,:] =  x0*np.cos(t) + v0*np.sin(t)
    out[1,:] = -x0*np.sin(t) + v0*np.cos(t)
    
    return out;

def sho_euler_implicit(x0, v0, tmax, h):
    N = int(tmax/h) + 1
    
    out = np.zeros((2,N))
    H = np.array([[1,h],[-h,1]])/(1+h**2)
    
    out[0,0] = x0
    out[0,1] = v0
    
    for i in range(1,N):
        out[:,i] = np.dot(H, out[:,i-1])
    
    return out;

def sho_euler_symplectic(x0, v0, tmax, h):
    N = int(tmax/h) + 1
    
    out = np.zeros((2,N))
    H = np.array([[1,h],[-h,1-h**2]])
    
    out[0,0] = x0
    out[0,1] = v0
    
    for i in range(1,N):
        out[:,i] = np.dot(H, out[:,i-1])
    
    return out;

