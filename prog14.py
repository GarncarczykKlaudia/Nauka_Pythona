produkty = {'ss1':{'nazwa':'sukienka','rozmiar':['xs','s','m','l']},
            'ss2':{'nazwa':'spodnie', 'rozmiar':[34,35]}}


for id in produkty:
    print(produkty[id]['nazwa'])
    for r in produkty[id]['rozmiar']:
        print(r)



#for id in produkty:
#    print(produkty[id]['rozmiar'])



#koszyk=[{'nazwa':'mleko' , 'cena':40},
#        {'nazwa':'maka', 'cena':50}]
