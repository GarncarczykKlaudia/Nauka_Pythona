rosliny=['sosna','jodla','krzew']
qty=[1,2,3]

for idx in range(len(rosliny)):
    print(rosliny[idx] + ":" + str(qty[idx]))


for idx in range(len(qty)):
    print(str(qty[idx]) + " to ilosc dla produktu:" + rosliny[idx])
