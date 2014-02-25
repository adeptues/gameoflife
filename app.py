#!/bin/python

# Python game of life by Thomas Helmkay
# rules:
# 1. Any live cell with fewer than two live neighbours dies,
# as if caused by under-population.
# 2.  Any live cell with two or three live neighbours lives 
# on to the next generation.
# 3.  Any live cell with more than three live neighbours dies,
# as if by overcrowding.
# 4. Any dead cell with exactly three live neighbours becomes a live
# cell, as if #by reproduction.

# text base input

from numpy import *
import time
import pygame, sys
from pygame.locals import *

#REMBER NUMPY ARGS A Y,X NOT X,Y
#10x10 grid
#grid_width = 100
#grid_height = 100
#grid = zeros((grid_height,grid_width))

#do somthing with pythons optional parameters to allow for test
#objects and if not resent fall back onto global grid object


pygame.init()
fpsClock =  pygame.time.Clock()
ws = pygame.display.set_mode((255,255))
# This sets the width and height of each grid location
width  = 20
height = 20
 
# This sets the margin between each cell
margin = 5

# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
runflag = False

def count_alive(cells):
    count = 0
    for i in cells:
        if(i == 1):
            count += 1
    return count

def count_dead(cells):
    count = 0
    for i in cells:
        if(i == 0):
            count += 1
    return count

def calculate_index(x,y,x_width):
    index = x+(y*x_width)
    return index


def build_coords(x,y):
    coords = []
    up = array([x,y-1])
    down = array([x,y+1])
    left = array([x-1,y])
    right = array([x+1,y])
    top_right = array([x+1,y-1])
    top_left = array([x-1,y-1])
    bt_right = array([x+1,y+1])
    bt_left = array([x-1,y+1])
    coords.append(up)
    coords.append(down)
    coords.append(left)
    coords.append(right)
    coords.append(top_left)
    coords.append(top_right)
    coords.append(bt_left)
    coords.append(bt_right)
    return coords

# gets all 8 neighbours of a cell
def get_neighbours(x,y,grid):
    coords = build_coords(x,y)
    neighbours = zeros(8)
    count = 0
    for item in coords:
        value = 0
        try:
            value = grid[item[0],item[1]]
        except IndexError:
            #TODO handle this error to tordial array
            pass
            
        neighbours[count] = value
        count += 1
    return neighbours

def tick(grid,x,y):
    cells = get_neighbours(x,y,grid)
    dead = count_dead(cells)
    alive = count_alive(cells)
    if grid[x,y] == 1:
        #apply rules 1 to 3
        if alive == 2 or alive == 3:
            return True
        elif alive < 2:
            #Any live cell with fewer than two live neighbours dies,
            # as if caused by under-population.
            return False
        elif alive > 3: #rule 3
            return False
    else:
        if alive == 3:
            return True
            

#render the grid either in text form or in graphics but point remains
#single render function    
def render(grid):
    renderStr = ""
    for row in grid:
        for elem in row:
            if elem == 0:
                renderStr + " "
            else:
                renderStr + "#"
        renderStr + "\n"
    print renderStr

def renderWindow(grid):
        # Draw the grid
    for row in range(10):
        for column in range(10):
            color = white
            if grid[row][column] == 1:
                color = green
            pygame.draw.rect(ws,
                             color,
                             [(margin+width)*column+margin,
                              (margin+height)*row+margin,
                              width,
                              height])

def run():
    grid = zeros((10,10))
    #initial pattern
#    grid[1,3] = 1
 #   grid[2,3] = 1
  #  grid[1,4] = 1
   # grid[2, 4] = 1
   #oscilator
    grid[3,1] = 1
    grid[4,1] = 1
    grid[5,1] = 1
    while True:
        if runflag:
            nextg = zeros((10,10))
            for y in range(10):
                for x in range(10):
                    alive = tick(grid,y,x)
                    if alive:
                        nextg[y,x] = 1
                    else:
                        nextg[y,x] = 0
            grid = nextg
            print grid
        renderWindow(grid)
        handle_events(grid)
        pygame.display.update()
        time.sleep(1)

def handle_events(grid):
    global runflag
    for event in pygame.event.get():
        if event.type == QUIT:
            print "exiting"
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            print "mouse coords"+str(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (width + margin)
            row = pos[1] // (height + margin)
            # Sete t hat location to zero
            if grid[row][column] == 1:
                grid[row][column] = 0
            else:
                grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE or event.key == K_q:
                pygame.event.post(pygame.event.Event(QUIT))
            if event.key == K_SPACE:
                if runflag:
                    runflag = False
                else:
                    runflag = True

def runtest(grid):
    while True:
        handle_events()
        renderWindow(grid)
        pygame.display.update()
    
# the rules need to be applied simultaneously not sequentially or
# compute all nesecary changes before updateing grid do not update
# prior to tick
if __name__ == '__main__':
    run()
    


