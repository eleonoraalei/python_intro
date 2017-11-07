# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 12:20:50 2017

@author: Federico Biondi
"""
import numpy as np

# ESERCIZI
##################################################
# Exercise 1:                                    #
# Create a 5x5 matrix with 5's on its diagonal   #
##################################################
print ('----------------------------------------')
print ('Ex 1')

# Solution 1
m = np.eye(5) * 5
print ('')
print (m)

# Solution 2
m = np.zeros((5, 5))
m[np.diag_indices_from(m)] = 5
print ('')
print (m)

##################################################
# Exercise 2                                     #
# Create a random array with 5 elements  v       #
# and replace its largest value with 0           #
##################################################
print ('----------------------------------------')
print ('Ex 2')

# Solution
r = np.random.random(5)
print ('')
print (r)

r[np.argmax(r)] = 0
print ('')
print (r)

##################################################
# Exercise 3:                                    #
# Create the following array                     #
'''                                              #
1 2 3 4 5                                        #
1 2 3 4 5                                        #
1 2 3 4 5                                        #
1 2 3 4 5                                        #  
1 2 3 4 5                                        #
'''                                              # 
##################################################
print ('----------------------------------------')
print ('Ex 3')

# Solution 1
a = np.ones((5, 5)) * np.arange(1, 6)
print ('')
print (a)

# Solution 2
a = np.ones(5)[:, np.newaxis] * np.arange(1, 6)
print ('')
print (a)


##################################################
# Exercise 4:                                    #
# Create a checkerboard (8x8, 0s and 1s)         #
'''                                              # 
0 1 0 1 0 1 0 1                                  #
1 0 1 0 1 0 1 0                                  #
0 1 0 1 0 1 0 1                                  #
1 0 1 0 1 0 1 0                                  # 
0 1 0 1 0 1 0 1                                  #
1 0 1 0 1 0 1 0                                  #
0 1 0 1 0 1 0 1                                  #
1 0 1 0 1 0 1 0                                  #
'''                                              #
##################################################
print ('----------------------------------------')
print ('Ex 4')

# Solution 
checkerboard = np.zeros((8, 8), dtype='i')
checkerboard[::2, 1::2] = 1
checkerboard[1::2, ::2] = 1
print ('')
print (checkerboard)


##################################################
# Exercise 5:                                    # 
# Extract the integer part of a random sample    #
##################################################
print ('----------------------------------------')
print ('Ex 5')

v = np.random.uniform(0, 10, 5)
print (v)

# Solution 1
sol = a - a%1
print ('')
print (sol)

# Solution 2
sol = np.floor(a)
print ('')
print (sol)

# Solution 3
sol = np.ceil(a) - 1
print ('')
print (sol)

# Solution 4
sol = np.trunc(a)
print ('')
print (sol)

# Solution 5
sol = a.astype(int)
print ('')
print (sol)


##################################################
# Exercise 6:                                    #
# Create an array with 10 equidistant numbers    #
# between 0 and 1, excluding 0 and 1             #
##################################################
print ('----------------------------------------')
print ('Ex 6')

a = np.linspace(0, 1, 12)[1:-1]
print ('')
print (a)


##################################################
# Exercise 7:                                    #
# Find the value closest to a given number       #
# in an array                                    #
##################################################
print ('----------------------------------------')
print ('Ex 7')

a = np.random.random(10)
print (a)
target = 0.23
sol = a[np.argmin(np.abs(a - 0.3))]
print ('')
print (sol)




















