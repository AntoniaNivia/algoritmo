#contar elemntos pares e impares de uma dada lista
a=[]
par=0
impar=0
for i in range(10):
    a.append(int(input("digite um numero:")))
    if a[i]%2==0:
        par+=1
    else:
        impar+=1
print("quantidade de numeros pares:", {par})
print("quantidade de numeros impares:", {impar})