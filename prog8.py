samochody=['polonez','syrena']

print(samochody[0])
print(samochody[1])
#print(samochody[2])

#petla1
print("petla1--------")
for s in samochody:
    print(s)

#petla 2

print("lpetla2----------")

for idx in [0,1]:
    print(samochody[idx])

print("z lenem")

print("len:{0}".format(len(samochody)))

print ("petla3---")

for idx in range(len(samochody)):
    print(samochody[idx])
