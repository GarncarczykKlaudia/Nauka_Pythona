a=input("Podaj produkty z listy: A:kasza, B:ogorek, C:ryz, D:maka: E:mleko oddzielajac przecinkiem")
print(a)

lista_zakupow=a.split(",")

print(lista_zakupow)

cena=[1,2,3,4,5]

b=len(lista_zakupow)

print(b)
cena_matryca = []


for idx in range(len(lista_zakupow)):
    print(lista_zakupow[idx])
    if lista_zakupow[idx]=='A':
            cena_matryca.append(cena[0])
    elif lista_zakupow[idx]=='B':
            cena_matryca.append(cena[1])
    elif lista_zakupow[idx]=='C':
            cena_matryca.append(cena[2])
    elif lista_zakupow[idx]=='D':
            cena_matryca.append(cena[3])
    elif lista_zakupow[idx]=='E':
            cena_matryca.append(cena[4])


print(cena_matryca)

suma=0.0

for idx in range(len(cena_matryca)):
     suma=suma+cena_matryca[idx]

print("wartosc koszyka przed obnizka: {0}".format(suma))


if 'kasza' in lista_zakupow and 'ogorek' in lista_zakupow:
    suma=suma-(suma*5)/100
print('wartosc koszykapo obnizce: {0}'.format(suma))
