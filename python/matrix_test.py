from matrix import *

tree = Matrix(3, 3)
tree.setRow(0, [1, 2, 3])
tree.setRow(1, [4, 5, 6])
tree.setRow(2, [7, 8, 9])
tree.printMat()


mat = tree.Determinant()
print (mat)




##tree.printMat()
##tree.setVal(1, 1, 4)
##tree.printMat()
##print (tree.getRow(1))
##print (tree.getCol(2))
