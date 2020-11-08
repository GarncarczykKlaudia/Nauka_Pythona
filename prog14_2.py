baza_danych={'a':{'index':'A001','PN':'322-1','czesci':['a','b','c']},
'b':{
            'index':'A002','PN':'321-0','czesci':['a','c']},
            'c':{
            'index':'A003','PN':'324-1','czesci':['x']}}


for id in baza_danych:
    print (baza_danych[id]['index'])
    for r in baza_danych[id]['czesci']:
        print(r)
