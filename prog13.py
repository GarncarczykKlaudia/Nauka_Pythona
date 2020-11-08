samolot={'name':'boeing',
         'typ':'pasazerski',
         'przebieg':1000.50}


print(samolot['name'])
print(samolot['typ'])
print(samolot['przebieg'])


# mozna dopisywac do slownika itemy np

samolot['silnik']='odrzutowy'

print(samolot.get('typ'))

#print petla po kluczu
print("petla po kluczu--------------------")
for klucz in samolot:
    print('{0}: {1}'.format(klucz,samolot[klucz]))

#petla klucz/wartosc

print("petla klucz/wartosc----------------")

for key,value in samolot.items():
    print("{0} {1}".format(key, value))
