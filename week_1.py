##Given an integral number, determine if it's a square number 

import math 

# Implied return 
def is_square(n):  
    if n < 0: 
        return False 
    sqrtn = math.sqrt(n)
    return sqrtn % 1 == 0

# Fully written return statement 
def is_square(n):  
    if n < 0: 
        return False 
    sqrtn = math.sqrt(n)
    if sqrtn % 1 == 0:
        return True
    else:
        return False  