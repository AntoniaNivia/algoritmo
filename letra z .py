a=[]
impar=0
total=0
for i in range(10):
    a.append(int(input("digite um numero:")))
    if a[i]%2!=0:
        impar+=1
    total+=1
print("a quantidade dos elemntos imapres:", impar)
print("o percentual de elementos impares é:", (impar/total)*100, "%")