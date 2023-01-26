
import numpy as np
import matplotlib.pyplot as plt




class MonteCarlo:


    def __init__(self, *args):

        self.lines = args[0]
        self.columns = args[1]
        self.rs = args[2]
        self.omega = np.arange(self.lines*self.columns).reshape((self.lines, self.columns))
        self.restriction = [self.omega[0, :], self.omega[self.lines-1,:], self.omega[:, 0], self.omega[:, self.columns-1]] # upper, lower, left, right
        self.matrix_columns = np.arange(self.columns)
        self.matrix_lines = np.arange(self.lines) 
        self.memory = [[(i, j) for j in range(self.columns)] for i in range(self.lines)]
    
    
    def check_availability(self):

        for i in range(int((self.lines*self.columns)/2)):
            random_variable_column = np.random.choice(self.matrix_columns, 1)[0]
            random_variable_line = np.random.choice(self.matrix_lines, 1)[0]
            self.memory[random_variable_line][random_variable_column] = (-random_variable_line, -random_variable_column) if (random_variable_line, random_variable_column) in self.memory[random_variable_line] else print("ok")







