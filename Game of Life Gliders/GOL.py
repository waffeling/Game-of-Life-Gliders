#!/usr/bin/env python
# coding: utf-8

get_ipython().run_line_magic('matplotlib')

# Making starting grid from an excel file (Big Boy data guy now aren't we?)
import math;
import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt;
import matplotlib.animation as animation;

gridsize = 20; 

time = 110;

Grid = np.zeros((gridsize, gridsize));
Decider = np.zeros((gridsize, gridsize));

#Import excel grid 
data = pd.read_excel(r'..\Game of Life Gliders\Grid10.xlsx', names = range(gridsize));

for i in range(gridsize):
    tempgrid = data[i];
    for j in range(gridsize):
        Grid[j][i] = tempgrid[j];

#Now we have to code the game. 

Nextgrid = Grid.copy();

#will help with efficiency counting neighbors
def permutation(i, j, gridsize):
    if (i==0):
        if(j==0):
            ilist = [gridsize-1, i, i+1];
            jlist = [gridsize-1, j, j+1];
            
        elif(j==gridsize-1):
            ilist = [gridsize-1, i, i+1];
            jlist = [j-1, j, 0];
    
        else:
            ilist = [gridsize-1, i, i+1];
            jlist = [j-1, j, j+1];
            
    elif (i==gridsize-1):
        if(j==0):
            ilist = [i-1, i, 0];
            jlist = [gridsize-1, j, j+1];
            
        elif(j==gridsize-1):
            ilist = [i-1, i, 0];
            jlist = [j-1, j, 0];
    
        else:
            ilist = [i-1, i, 0];
            jlist = [j-1, j, j+1];
                     
    else:
        if(j==0):
            ilist = [i-1, i, i+1];
            jlist = [gridsize-1, j, j+1];
            
        elif(j==gridsize-1):
            ilist = [i-1, i, i+1];
            jlist = [j-1, j, 0];
    
        else:
            ilist = [i-1, i, i+1];
            jlist = [j-1, j, j+1];
    
    finallist = [];
    for u in range(3):
        for v in range(3):
            finallist.append([ilist[u], jlist[v]]);
            
    return finallist

#function to count neighbors around a certain block (i,j)         
def count(i, j, grid, gridsize):
    ijlist = permutation(i, j, gridsize);
    count = 0;
    
    for k in range(9):
        if (grid[ijlist[k][0], ijlist[k][1]] == 1):
            count += 1;
            
    if (Grid[i][j] == 1):
        count -= 1;
        
    return count

#function to scan through the grid to make the decider 
def makedecider(grid, decider, gridsize):
    for i in range(gridsize):
        for j in range(gridsize):
            decider[i][j] = count(i, j, grid, gridsize);
            
#Time to start animating:

#Generate scene:
fig = plt.figure();
axs = plt.axes();

#Make a list to conatin all of the plots to be iterat
img = [];

Map = axs.imshow(Grid);

for t in range(time):
    
    makedecider(Grid, Decider, gridsize); 
    
    #Making next grid by applying rules
    for i in range(gridsize):
        for j in range(gridsize):
            if(Grid[i][j] == 1 and (Decider[i][j] == 2 or Decider[i][j] ==3)):
                Nextgrid[i][j] = 1;
            
            elif(Grid[i][j] == 0 and Decider[i][j] ==3):
                Nextgrid[i][j] = 1;
                
            else:
                Nextgrid[i][j] = 0;
    #Moving grids:

    Grid = Nextgrid.copy();
    Decider = np.zeros((gridsize, gridsize));
    Map.set_data(Grid);
    img.append([plt.imshow(Grid)]);
    


anim = animation.ArtistAnimation(fig, img,
                            interval = 50, 
                            repeat_delay = 300,
                            blit = True);
    
plt.show();


# In[ ]:




