from random import randint

#declaring constants
#ZERO - bin_char '0'
#ONE - bin_char '1'
ZERO = '0'
ONE = '1'

#convert binary number to decimal
#imput:string of binary
#output: decimal int
def decimal(binstr):
    d = 0
    for i in range(len(binstr)):
        place = int(binstr[(len(binstr)-1)-i]) * 2**i
        d = d + place
    return d

#add 3 binary characters
#input: 3 bin_chars
#output: carryover and answer (bin_chars)
def __addBit(x, y, z):
    if x+y+z in ['111']:
        a = ONE
        c = ONE
    if x+y+z in ['110', '101', '011']:
        a = ZERO
        c = ONE
    if x+y+z in ['100', '010', '001']:
        a = ONE
        c = ZERO
    if x+y+z in ['000']:
        a = ZERO
        c = ZERO
    return (c, a)

#fill 0's in binary number to match length
#input: length of longer string, short string
#output: the short string filled
def __fill(length, short):
    ret = short
    for i in range(length - len(short)):
        ret = ZERO + ret
    return ret

#add 2 binary strings
#input: 2 strings of binary
#output: a string containing the answer in binary
def add(s1, s2):
    if len(s1) > len(s2):
        long = s1
        short = s2
    else:
        long = s2
        short = s1
    short = __fill(len(long), short)
    carry = ZERO
    ans = ''
    for i in range(len(long)):
        #print (i, long[(len(long)-1)-i], short[(len(ans)-1)-i], carry, long, short)
        (carry, result) = __addBit(long[(len(long)-1)-i], short[(len(short)-1)-i], carry)
        ans = result + ans
        #print (carry, ans)
        #print ('')
    if carry == ONE:
        ans = carry + ans
    return ans
        
#print (add('101', '11'))
    
for i in range(100):
    (test1, test2) = (randint(1, 10000), randint(1, 10000))
    test = add(bin(test1)[2:], bin(test2)[2:])
    if test == bin(test1 + test2)[2:]:
        print ("fail: num1 = "+bin(test1)[2:]+" , num2 = "+bin(test2)[2:]+" , expected = "+bin(test1 + test2)[2:]+" , add = "+test)
    
               
            
    
        
        

    
