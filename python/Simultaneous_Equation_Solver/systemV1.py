
# Solve system using Cramer's rule
# input: number of variables, equations of form a, b, c, d, e, ... (coefficients)
# Output: (x, y, z, ...)

#_______________________________________________________
from matrix import *
import sys

num_vars = int(input("How many variables?"))
if num_vars <= 1:
    print ("Error: number of variables should be >= 2")
    sys.exit(1)
equations = Matrix(num_vars, num_vars + 1)

for i in range(num_vars):
    e = input("Equation #%s" %((i+1))) #As a list of ints
    f = [int(s.strip()) for s in e.split(',')]
    if len(f) != num_vars + 1:
        print ("Error: input incorrect length")
        sys.exit(1)
    equations.setRow(i, f)
    
#print (num_vars)
#equations.printMat()

D = Matrix(num_vars, num_vars)
for i in range(num_vars):
    c = equations.getCol(i)
    D.setCol(i, c)
#D.printMat()
Dvar = []
for i in range(num_vars):
    Di = D.copy()
    Di.setCol(i, equations.getCol(num_vars))
    Dvar.append(Di)
#for mat in Dvar:
#    mat.printMat()

if D.Determinant() == 0:
    if all(item.Determinant() == 0 for item in Dvar):
        print ("Error: System dependant")
        sys.exit(1)
    else:
        print ("Error: System inconsistant")
        sys.exit(1)
else:
    solution = []
    for i in Dvar:
        ans = (i.Determinant()) / (D.Determinant())
        solution.append(ans)
    print (solution)
            


    
    



    



        
