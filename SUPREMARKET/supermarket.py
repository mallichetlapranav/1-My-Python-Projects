from datetime import datetime

name=input("Enter your name;")

lists='''
rice    Rs 20/kg
sugar   Rs 30/kg
salt    Rs 50/kg
maggi   Rs 50/kg
oil     Rs 100/liter
paneer  Rs 150/kg
Boost   Rs 90/each
colgate Rs 85/each
'''
#decleration
price=0
pricelist=[]
totalprice=0
Finalfinalprice=0
ilist=[]
qlist=[]
plist=[]

#rates for items
items={"rice":20,
"sugar":30,
"salt":50,
"maggi":50,
"oil":100,
"panner":150,
"Boost":90,
"colgate":85} 
option=int(input("for list of items press 1"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit:"))
    if inp1==2:
     break
    if inp1==1:
        item=input("Enter your items:")
        quantity=int("Enter quantity:")
        if item in items.keys():
            price=quantity*(items(item))
            pricelist.append(item,quantity,items,price)
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
           print("Sorry you entered item isnot available")
    else:
       print("You entered wrong number")
    imp=input("can i bill the items yes or no:")
    if imp=='yes':
       pass
    if finalamount!=0:
       print(25*"=","pranav supermarket",25*"=")
       print(28*" ","palamaner")
       print("Name:",name,30*" ","Date:",datetime.now)
       print(75*"-")
       print("sno",8*" ",'items',8*" ",'quantity',3*" ",'price')
    for i in range(len(pricelist)):
       print(i, 8 * ' ', 5 * ' ', ilist[i], 3 * ' ', qlist[i], 8 * " ", plist[i])
    print(75*"-")
    print(50*" ",'Totalamount:','Rs',totalprice)
    print("gst amount",50*" ",'Rs',gst)
    print(75*"-")
    print(50*" ",'finalamount:','Rs',finalamount)
    print(75*"-")
    print(50*" ","Thank you for visiting")
    print(75*"-")   
