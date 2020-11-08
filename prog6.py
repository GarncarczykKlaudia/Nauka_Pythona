# imie='Ala'
# zwierze='kot'
# ile=6
#
# if ile==1:
#     print('{0} ma  {1}a'.format(imie,zwierze))
# else:
#     print('{0} ma {1} {2}ow'.format(imie,ile,zwierze))


imie = 'Klaudia'
produkt = 'toreb'
ilosc = 1

if ilosc>=10:
    print('{0} kupiala {1} {2}ek'.format(imie,ilosc,produkt))
elif ilosc==1:
    print ('{0} kipla {1} {2}ke'.format(imie, ilosc, produkt))
else:
    print ('{0} kupila {1} {2}ki'.format(imie,ilosc,produkt))
