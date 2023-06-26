"""
Created on Tue Jun 20 2023

Description: A class that draw shapes using the 'turtle' Module

@author: Ethan Xia
"""

import turtle

class DrawShapes:
    
    # Creating the Init function
    def __init__(self, Shape):
        self.Shape = Shape
        # Give each shape more information and print it out
        if Shape == 'Circle' or 'circle':
            print('Shape = Circle, Side/s = 0, Vertice/s = 0, Interior Angle = NA')
        if Shape == 'Triangle' or 'triangle':
            print('Shape = Triangle, Side/s = 3, Vertice/s = 3, Interior Angle = 60')
        if Shape == 'Square' or 'square':
            print('Shape = Square, Side/s = 4, Vertice/s = 4, interior Angle = 90')
        if Shape == 'Rectangle' or 'rectangle':
            print('Shape = Rectangle, Side/s = 4, Vertice/s = 4, Interior Angle = 90')
        if Shape == 'Hexagon' or 'hexagon':
            print('Shape = Hexagon, Side/s = 6, Vertice/s = 6, Interior Angle = 120')
        if Shape == 'Octagon' or 'Octagon':
            print('Shape = Octagon, Side/s = 8, Vertice/s = 8, Interior Angle = 45')
        if Shape == 'Star' or 'star':
            print('Shape = Star, Side/s = Varies, Vertice/s = Varies, Interior Angle = Varies')
        
    # Creating the Circle function
    def Circle(self, Size, Filled):
        if Filled == True:
            turtle.begin_fill()
        turtle.circle(Size)
        if Filled == True:
            turtle.end_fill()
         
    # Creating the Triangle function
    def Triangle(self, Size, Filled):
        if Filled == True:
            turtle.begin_fill()
        turtle.back(Size)
        turtle.left(60)
        turtle.forward(Size)
        turtle.right(120)
        turtle.forward(Size)
        turtle.right(120)
        if Filled == True:
            turtle.end_fill()
                
    # Creating the Square function       
    def Square(self, Size, Filled):
        if Filled == True:
           turtle.begin_fill()
        for i in range(4):
            turtle.forward(Size)
            turtle.left(90)
        if Filled == True:
            turtle.end_fill()
    
    # Creating the Rectangle function        
    def Rectangle(self, Width, Length, Filled):
        if Filled == True:
           turtle.begin_fill()
        turtle.forward(Length)
        turtle.right(Width)
        turtle.forward(Length)
        turtle.right(Width)
        turtle.forward(Length)
        turtle.right(Width)
        turtle.forward(Length)
        turtle.right(Width)
        if Filled == True:
            turtle.end_fill()
            
    # Creating the Hexagon function        
    def Hexagon(self, Size, Filled):
        if Filled == True:
            turtle.begin_fill()
        for i in range(6):
            turtle.forward(Size)
            turtle.left(60)
        if Filled == True:
            turtle.end_fill()
            
    # Creating the Octagon function       
    def Octagon(self, Size, Filled):
        if Filled == True:
            turtle.begin_fill()
        for i in range(8):
            turtle.forward(Size)
            turtle.left(45)
        if Filled == True:
            turtle.end_fill()
            
    # Creating the Star function        
    def Star(self, Size, Points, Filled):
        if Filled == True:
            turtle.begin_fill()
        for i in range(1, Points+1):
            turtle.forward(Size)
            if i % 2 == 0:
                turtle.left(175)
            else:
                turtle.left(225)
            if Filled == True:
                turtle.end_fill()
                