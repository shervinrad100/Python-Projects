''' Create a class called unit with input, output
make subclasses such as a mixer and CSTR and solve for parameters '''

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


class VarType:
    def __init__(self,loLim, upLim, units=None):
        self.loLim = loLim
        self.upLim = upLim
        self.units = units
                  
    def __str__(self):
        return "Lower limit: " + str(self.loLim) + '\n' + "Upper Limit: " + str(self.upLim)+ '\n' + "Units: "+ str(self.units)
    
    
class Model():
    def __init__(self, params):
        self.params = params 
    
''' idk how to go about it because:
    1. to solve simultaneous equations, you need to make the matrix
        1.1 BUT if you have differentials then thats different
       but i dont want them to input the matrix by hand and i want to infer that from the equations they input (fml)
    2. if you wanna solve differential then you need to define a function and use scipy.integrate for that
       i cant have them define that as an input into the application. They can only do it if they write it straight
       into the source code. 
      
        