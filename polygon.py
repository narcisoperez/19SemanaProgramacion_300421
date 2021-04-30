# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 12:07:34 2021

@author: NarW10
"""


class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])
            
class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)

    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s =(a + b + c) / 2
        area =(s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('El area del triangulo es %0.2f' %area)
        
#Defino el objeto
t = Triangle()
#Ingreso valores
t.inputSides()
t.findArea()