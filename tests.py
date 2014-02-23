#!/bin/python

#unit tests for app.py

import unittest
from app import *
from numpy import *


class GameOfLifeTests(unittest.TestCase):
    
    def test_build_coords(self):
        x = 1
        y = 2
        coords = build_coords(x,y)
        coord = coords[0]
        self.assertTrue(array_equal(coord,[1,1]))
        coord = coords[1]
        self.assertTrue(array_equal(coord,[1,3]))
        coord = coords[2]
        self.assertTrue(array_equal(coord,[0,2]))
        coord = coords[3]
        self.assertTrue(array_equal(coord,[2,2]))
        coord = coords[4]
        self.assertTrue(array_equal(coord,[0,1]))
        coord = coords[5]
        self.assertTrue(array_equal(coord,[2,1]))
        coord = coords[6]
        self.assertTrue(array_equal(coord,[0,3]))
        coord = coords[7]
        self.assertTrue(array_equal(coord,[2,3]))
        
    def test_get_neighbours(self):
        x,y = 1,2
        width,height = 4,4

        grid = zeros((width,height))
        grid[1,1] = 1 #up
        grid[2,3] = 1 # bottom rigth
        grid[0,3] = 1 #bottom left
        neighbours = get_neighbours(x,y,grid)
        self.assertEqual(neighbours[0],1)
        self.assertEqual(neighbours[7],1)
        self.assertEqual(neighbours[6],1)
        self.assertEqual(neighbours[1],0)
        self.assertEqual(neighbours[2],0)
        self.assertEqual(neighbours[3],0)
        self.assertEqual(neighbours[4],0)
        self.assertEqual(neighbours[5],0)
        
    #toridal test
    def test_get_neighbours2(self):
        x,y = 1,0
        width,height = 4,4

        grid = zeros((width,height))
        grid[0,0] = 1 
        grid[1,1] = 1
        grid[1,3] = 1 #tordial exists on opposite side of grid
        neighbours = get_neighbours(x,y,grid)
        self.assertEqual(neighbours[0],1)
        self.assertEqual(neighbours[1],1)
        self.assertEqual(neighbours[2],1)
        
    def test_count_alive(self):
        cells = [1,0,1,0,1,0,1,1]
        expected = 5
        actual = count_alive(cells)
        self.assertEqual(actual,expected)

    def test_count_dead(self):
        cells = [1,0,1,0,1,0,1,1]
        expected = 3
        actual = count_dead(cells)
        self.assertEqual(actual,expected)


        

if __name__ == '__main__':
    unittest.main()
    
#purley for dev mode in emacs

