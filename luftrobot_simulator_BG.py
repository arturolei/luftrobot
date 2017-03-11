#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 22:43:27 2017

@author: bethanygarcia
"""

NORTH, SOUTH, EAST, WEST =  0, 180, 90, 270


class Robot:
    def __init__(self, bearing=NORTH, x=0, y=0):
        self._x = x
        self._y = y
        self.bearing = bearing
        self._instructions = {'A': self.advance, 
                              'L': self.turn_left,
                              'R': self.turn_right}
    
 
    @property
    def coordinates(self):
        return (self._x, self._y)
    
    
    def advance(self):
        moves = {NORTH: 1, SOUTH: -1, EAST: 1, WEST: -1}
        
        if self.bearing in (NORTH, SOUTH):
            self._y += moves[self.bearing]
            
        if self.bearing in (EAST, WEST):
            self._x += moves[self.bearing]
    
     
    def turn_left(self):
        self.bearing = (self.bearing + 270) % 360
    
    
    def turn_right(self):
        self.bearing = (self.bearing + 90) % 360
    
    
    def simulate(self, directions):
        try:
            for item in directions:
                self._instructions[item]()
        except ValueError as err:
            print(err)




class Luftrobot(Robot):
    def __init__(self, bearing=NORTH, x=0, y=0, z=0):
        super().__init__(bearing, x, y)
        self._z = z
        self._instructions['B'] = self.goback
        self._instructions['U'] = self.ascend
        self._instructions['D'] = self.descend
    
    
    @property
    def coordinates(self):
        return (self._x, self._y, self._z)
    
    
    def goback(self):
        moves = {NORTH: -1, SOUTH: 1, EAST: 1, WEST: -1}
        
        if self.bearing in (EAST, WEST):
            self._y += moves[self.bearing]
            
        if self.bearing in (NORTH, SOUTH):
            self._x += moves[self.bearing]
     
    def ascend(self):
        self._z += 1
    
    def descend(self):
        self._z -= 1
        
        if self._z < 0:
            raise ValueError("FYI, I CAN'T DESCEND INTO GROUND, IDIOT")
            
        self._z = 0
            
    def warp(self, x):
        self._x = x
    
    