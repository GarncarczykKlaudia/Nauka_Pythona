imie= input("Podaj swoje imie")

print("Witaj " + imie)

client_list=['Fiat','Avio','TRW','Pitney']
product_list=['sap','ms']
order_qty=[1,2,3,4]
order_list=['sap','ms','ms','sap']

print ("Nas glowni klienci to:")
for s in client_list:
    print(s)

print("wszystkie nasze produkty to:")
for idx in range(len(product_list)):
    print(product_list[idx])

print("Nasze obecne zamowienia:")

for idx in range(len(order_list)):
     print(order_list[idx] + ":" +str(order_qty[idx]))
