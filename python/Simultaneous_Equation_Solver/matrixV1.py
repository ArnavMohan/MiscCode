
#init, fill, add, sum,mult, transpose, determinant, sum_product

#_________________________________________________________________
class Matrix: #TODO replace errors with method error, better error descriptions
    num_rows = 0#TODO improve printing -- __printRow with string manipulation
    num_cols = 0
    
    def __init__(self, r, c=0):
        if r < 1 or c < 0:
            print ("Dimentions are negative.")
        else:
            self.rows = {}
            self.cols = {}
            self.num_rows = r
            self.num_cols = r if (c == 0) else c

        for i in range(r):
            self.rows[i] = []
            for j in range(c):
                self.rows[i].append(0)
        for i in range(c):
            self.cols[i] = []
            for j in range(r):
                self.cols[i].append(0)
    def Error(self, s):
        print (s)
        sys.exit(1)

    def setRow(self, r, row):
        if r in range(self.num_rows) and len(row) == self.num_cols:
            for i in range(self.num_cols):
                self.setVal(r, i, row[i])
        else:
            print ("Args not in range")
            
    def setCol(self, c, col):
        if c in range(self.num_cols) and len(col) == self.num_rows:
            for i in range(self.num_rows):
                self.setVal(i, c, col[i])
        else:
            print ("Args not in range")
                        
    def setVal(self, r, c, val):
        if r in range(self.num_rows) and c in range(self.num_cols):
            self.rows[r][c] = val
            self.cols[c][r] = val
        else:
            print ("Args not in range")
            
    def getVal(self, r, c):
        if r in range(self.num_rows) and c in range(self.num_cols):
            return self.rows[r][c]
        else:
            print ("Args not in range")

    def getRow(self, r):
        if r in range(self.num_rows):
            copy = []
            for item in self.rows[r]:
                copy.append(item)
            return copy
        else:
            print ("Args not in range")

    def getCol(self, c):
        if c in range(self.num_cols):
            copy = []
            for item in self.cols[c]:
                copy.append(item)
            return copy
        else:
            print ("Args not in range")

    def __printRow(self, l):
        s = "| "
        for i in l:
            s += " %5d" %(i)
        s += " |"
        return s

    def printMat(self):
        for r in range(self.num_rows):
            print (self.__printRow(self.getRow(r)))
        print ()

    #args: matrix, returns new matrix with sum of previous 2
    def add(self, matrix):
        if (self.num_rows, self.num_cols) != (matrix.num_rows, matrix.num_cols):
            print ("Matrix dimensions do not match")
        else:
            matrix.printMat()
            result = Matrix(self.num_rows, self.num_cols)
            matrix.printMat()
            for i in range(self.num_rows):
                for j in range(self.num_cols):
                    result.setVal(i, j, self.getVal(i, j) + matrix.getVal(i, j))
            return result
        
    def sub(self, matrix):
        if (self.num_rows, self.num_cols) != (matrix.num_rows, matrix.num_cols):
            print ("Matrix dimensions do not match")
        else:
            result = Matrix(self.num_rows, self.num_cols)
            for i in range(self.num_rows):
                for j in range(self.num_cols):
                    result.setVal(i, j, self.getVal(i, j) - matrix.getVal(i, j))
            return result
        
    def transpose(self):
        result = Matrix(self.num_cols, self.num_rows)
        for i in range(self.num_rows):
            result.setCol(i, self.getRow(i))
        return result
    
    def mult(self, matrix):
        if self.num_cols != matrix.num_rows:
            self.Error("Dimensions for matrix multiplications are not valid")
        result = Matrix(self.num_rows, matrix.num_cols)
        for i in range(self.num_rows):
            for j in range(matrix.num_cols):
                val = self.__sumProduct(self.getRow(i), matrix.getCol(j))
                result.setVal(i, j, val)
        return result
    
    def __sumProduct(self, l1, l2):
        if len(l1) != len(l2):
            self.Error("Lengths of the matricies are not equal.")
        result = 0
        for i in range(len(l1)):
            result += l1[i] * l2[i]
        return result
    
    def __isSquare(self):
        if self.num_rows - self.num_cols == 0:
            return True
        else:
            return False
        
    def Determinant(self): #Add error
        if (self.num_rows, self.num_cols) == (2, 2):
            return (self.getVal(0, 0) * self.getVal(1, 1)) - (self.getVal(0, 1) * self.getVal(1, 0))
        else:
            result = 0
            for i in range(self.num_cols):
                result += self.getVal(0, i) * self.__subDeterminant(i).Determinant()
            return result

    def __subDeterminant(self, i):
        mat = Matrix(self.num_rows - 1, self.num_rows - 1)
        for j in range(self.num_cols - 1):
            new_col = self.getCol((j+i+1)%(self.num_cols))
            new_col.pop(0)
            mat.setCol(j, new_col)
        return mat

    def copy(self):
        new = Matrix(self.num_rows, self.num_cols)
        for i in range(self.num_rows):
            new.setRow(i, self.getRow(i))
        return new
    
            
            
        
            
    
        
        
                
                    
        
        
    



    

    
        
        
            
        
            
        
        
        
