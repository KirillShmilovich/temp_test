"""
temp_test.py
description

Handles the primary functions
"""
import numpy as np
from temp_test import temp_cpp

class Temp():

    def __init__(self, temp_f):
        self.temp_f = np.asarray(temp_f)

    def convert_to_c(self):
        return (self.temp_f - 32.) * (5. / 9.)

    def convert_to_k(self):
        cel = self.convert_to_c()
        return cel + 273.15
    
    def convert_matrix_to_c_cpp(self):
        return temp_cpp.convert_matrix(np.atleast_1d(self.temp_f))

    def convert_vector_to_c_cpp(self):
    	return temp_cpp.convert_vector(self.temp_f)
