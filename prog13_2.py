dane_osobowe={'imie':'Klaudia',
                'naziwsko':'Garncarczyk',
                'pesel': 1000001 ,
                'kraj':'Polska'}

print ("Test")

for key,value in dane_osobowe.items():
    print("{0} {1}".format(key,value))

print ("inna metoda-----")

for key in dane_osobowe:
    print("{0} {1}".format(key, dane_osobowe[key]))


print("sprawdzian 1")

for key in dane_osobowe:
    print('{0} {1}'.format(key,dane_osobowe[key]))

print ("sprawdzian 2--------------")

for key,value in dane_osobowe.items():
    print("{0} {1}".format(key,value))
