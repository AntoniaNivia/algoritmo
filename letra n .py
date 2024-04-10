a=[]
for i in range (10):
    a.append(float(input(f"digite a {i+1}o, temperatura em graus celsius:")))
a.sort()
print(" a menor temperatura é:", a[0])
print("a maior temperatura é:", a[9])
print("a media das temperaturas é:", sum(a)/10)