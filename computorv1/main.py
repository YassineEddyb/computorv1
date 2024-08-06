import sys
import re

# get the polinomial equation from the arguments
equations = sys.argv[1].split(" = ")

# get the two equation seperated by =
equations_1 = equations[0]
equations_2 = equations[1]

# split the terms with + and -
equation_1_terms = re.split(" - | \+ ", equations_1)
equation_2_terms = re.split(" - | \+ ", equations_2)

# print the terms
print(equation_1_terms)
print(equation_2_terms)

# the approach is not very efficient becuase you need to simplify the equation 
# and you should  take into acount the signs separating the terms my toughts 
# is to split terms while keeping the signs so you can simplify the equation
# and the create two classes one to solve the second degree and one to solve
# the first degree.
