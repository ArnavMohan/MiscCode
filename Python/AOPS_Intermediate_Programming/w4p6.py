class Fraction:
    '''represents fractions'''

    def __init__(self, num, denom):
        '''Fraction(num, denom) -> Fraction
        creates the fraction object representing numerator / denominator'''
        if denom == 0:
            raise ZeroDivisionError
        #initialize attributes
        self.num = num
        self.denom = denom
        #checks for double negative fraction
        if self.num < 0 and self.denom < 0:
            self.num = abs(self.num)
            self.denom = abs(self.denom)
        #checks for negative denominator
        elif self.denom < 0:
            self.denom = abs(self.denom)
            self.num = -1*self.num
        #checks for simplification: case1    
        if self.num < self.denom:
            for i in range(2, abs(self.num)+1):
                if self.num % i == 0 and self.denom % i == 0:
                    self.num = int(self.num / i)
                    self.denom = int(self.denom / i)
        #case2
        elif self.num > self.denom:
            for i in range(2, abs(self.denom)+1):
                if self.num % i == 0 and self.denom % i == 0:
                    self.num = self.num / i
                    self.denom = self.denom / i

    def __str__(self):
        '''prints the fraction'''
        return str(self.num)+'/'+str(self.denom)

    def __float__(self):
        '''converts fraction to decimal'''
        return self.num / self.denom

    def __add__(self, other):
        '''Fraction + Fraction -> Fraction
        returns added fraction in simplest terms'''
        if self.denom == other.denom:
            return Fraction(self.num + other.num, self.denom)
        common_denom = self.denom * other.denom
        result_num = self.num * other.denom + other.num * self.denom
        return Fraction(result_num, common_denom)

    def __sub__(self, other):
        '''Fraction - Fraction -> Fraction
        returns subtracted fraction in simplest terms'''
        if self.denom == other.denom:
            return Fraction(self.num - other.num, self.denom)
        common_denom = self.denom * other.denom
        result_num = self.num * other.denom - other.num * self.denom
        return Fraction(result_num, common_denom)

    def __mul__(self, other):
        '''Fraction * Fraction -> Fraction
        returns multiplied fraction in simplest terms'''
        return Fraction(self.num*other.num, self.denom*other.denom)

    def __truediv__(self, other):
        '''Fraction / Fraction -> Fraction
        returns divided fraction in simplest terms'''
        reciprocal = Fraction(other.denom, other.num)
        return self * reciprocal

    def __eq__(self, other):
        '''Fraction == Fraction -> Boolean
        checks if Fraction equal to Fraction'''
        if self.num == other.num and self.denom == other.denom:
            return True
        else:
            return False

    


    
        
