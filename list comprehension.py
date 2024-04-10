#a parte interna cria uma linha e a parte externa cria uma lista de linhas

import random
a=[]
b=[]
c=[]
for i in range(5):   # controlando as linhas
    a.append([])
    b.append([])
    c.append([])
    for j in range (3):
        a[i].append(random.randint(0,10)) 
        b[i].append(random.randint(0,10)) 
        c[i].append(a[i][j] + b[i][j])
print(a)
print(b)
print(c)
    





































