from random import *
faces = ['head', 'tail']

head_count = 0
tail_count= 0
for i in range(10000):
    index = randint(0, 1)
    if faces[index] == 'head':
        head_count += 1
    else:
        tail_count += 1

print (str(head_count / 10000))
