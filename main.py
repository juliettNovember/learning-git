numbers=range(1,100)
podzielne=[]
potega=[]

for number in numbers:
    if (number % 5 ==0):
        potęga=number**3
        podzielne.append(number)
        potega.append(number**3)

print(podzielne,"\n",potega)
print("Napis")
print("Kolejny testowy napis")
