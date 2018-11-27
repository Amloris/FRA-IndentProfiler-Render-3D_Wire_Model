#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import FileIO
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def main():
    #Select File
    fname = FileIO.GetFile('./Data')
    
    #Load Data
    r_data = np.loadtxt(fname, delimiter=',', skiprows=13)
    
    #Plot Heatmap
    plt.figure(1)
    plt.imshow(r_data)
    plt.show(1)
    
    #3D Model
    spatial_reolution = 0.02   #mm per point
    z_span = np.arange(0., np.shape(r_data)[1]*spatial_reolution, spatial_reolution)
    theta_span = np.linspace(0., 360., np.shape(r_data)[0])
        
    x_data =  np.empty(np.shape(r_data))
    y_data = np.empty(np.shape(r_data))
    z_data = np.tile(z_span, (np.shape(r_data)[0], 1))
    
    for i in range(0,np.shape(r_data)[0]):
        x_data_temp = r_data[i,:]*np.cos(np.deg2rad(theta_span[i]))
        y_data_temp = r_data[i,:]*np.sin(np.deg2rad(theta_span[i]))
        
        x_data[i,:] = x_data_temp
        y_data[i,:] = y_data_temp
        
    '''
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = 0.5 * np.outer(np.cos(u), np.sin(v))
    y = 0.1 * np.outer(np.sin(u), np.sin(v))
    z = 0.2 * np.outer(1, np.cos(v))
    T = (x**2+y**2+z**2)**(1/2)
    ax.plot_surface(x, y, z, rstride=1, cstride=1, facecolors=cm.jet(T/float(T.max())))
    '''
    
    
    fig = plt.figure(2)
    ax = fig.add_subplot(111, projection='3d')    
    #ax.plot_surface(x_data, y_data, z_data, facecolors=plt.cm.viridis(r_data/float(r_data.max())), ccount=200, rcount=180)
    ax.plot_surface(x_data, y_data, z_data, facecolors=plt.cm.viridis((r_data-r_data.min())/float(r_data.max()-r_data.min())), ccount=180, rcount=400)
    #ax.plot_wireframe(x_data, y_data, z_data, color='k', linewidth= 0.1, ccount=800, rcount=180) 
    #ax.contourf(x_data, y_data, z_data, facecolors=plt.cm.viridis(r_data/float(r_data.max())))
   
    max_range = np.array([x_data.max()-x_data.min(), y_data.max()-y_data.min(), z_data.max()-z_data.min()]).max() / 2.0
    mid_x = (x_data.max()+x_data.min()) * 0.5
    mid_y = (y_data.max()+y_data.min()) * 0.5
    mid_z = (z_data.max()+z_data.min()) * 0.5
    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(mid_z - max_range, mid_z + max_range)

    plt.show(2)

'''Functions'''
'''--------------------------------------------------------------------------'''


if __name__ == "__main__":
    main()