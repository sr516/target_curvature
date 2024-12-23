import matplotlib.pyplot as plt
import numpy as np

import matplotlib
matplotlib.use('TkAgg')

# Need this for the colorbars we will make on the mirrored plot
from mpl_toolkits.axes_grid1 import make_axes_locatable


fig, (ax)= plt.subplots(1, 1, figsize=(5.0,5.0))

# Plot asteroid 
x0 = np.loadtxt('bg_06_xx.txt', delimiter = ' ')
y0 = np.loadtxt('bg_06_yy.txt', delimiter = ' ')
Den = np.loadtxt('bg_06_Den.txt', delimiter = ' ')


p1 = ax.pcolormesh(-x0,y0, Den, cmap=('gray_r'), vmin=0.,vmax=3, rasterized=True)
p2 = ax.pcolormesh(x0,y0, Den, cmap=('gray_r'), vmin=0., vmax=3, rasterized=True)

# Plot ejection angle
data = np.loadtxt('prov_06.txt', delimiter = ' ')

x_plot, y_plot, ang, vv = data[:, 0], data[:, 1], data[:, 2], data[:, 3]


ax.scatter(x_plot, y_plot, c = ang,
                 s=0.02, rasterized=True, vmin = 40, vmax = 80)
                 
ax.scatter(-x_plot, y_plot, c = ang,
                 s=0.02, rasterized=True, vmin = 40, vmax = 80)
                 
                 
fig.subplots_adjust(right=0.8)
cbar_ax = fig.add_axes([0.99, 0.35, 0.03, 0.3])
fig.colorbar(p1, cax=cbar_ax, label=r'Ejection angle, $\theta$ [degrees]')
   
   
# Set limit for axes	
ax.set_ylim([-20,20])
ax.set_xlim([-60,60])
ax.set_aspect('equal') 
    
ax.set_xlabel('x [m]')
ax.set_ylabel('z [m]')
	 	               
fig.tight_layout() 
fig.savefig('prov_test.png', bbox_inches='tight', dpi=350)               
