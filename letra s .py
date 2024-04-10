a, b, c=[], [], []
#atribuindo elementos a lista a 
cont=0
print("inserindo itens da tabela A")
while cont<6:
    n=int(input("digite um numero par:") )
    if n%2==0:
        a.append(n)
        cont+=1
    else:
        print("numero ímpar")
#atribuindo elementos a lista b
print("inserindo itens da tabela B")
cont=0
while cont<6:
    n=int(input("digite um numero ímpar:") )
    if n%2!=0:
        b.append(n)
        cont+=1
    else:
        print("numero par")
c=a+b
print(c)
