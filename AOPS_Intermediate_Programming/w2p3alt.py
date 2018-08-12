storage = {}
def catalan(n):
    if n == 0:
        return 1
    elif n in storage:
        return storage[n]
    else:
        total = 0
        for i in range(n):
            num1 = catalan(i)
            num2 = catalan(n-i-1)
            total = total + num1*num2
        storage[n] = total
        return total
print (catalan(993))





                
                
