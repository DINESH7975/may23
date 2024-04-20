from datetime import datetime
print("welcome to super market bill generation")

name = input("enter your name:")

#list of items

list_items = '''
rice      Rs 60/kg
sugar     Rs 40/kg
maggie    Rs 40/kg
cologate  Rs 90/kg
panner    Rs 110/kg
salt      Rs 20/kg
boost     Rs 90/kg
oil       Rs 160/liter
'''

#declaration

price = 0
price_list = []
total_price = 0
final_price = 0

item_list = []
quantity_list = []
p_list = []

#rates for item
items = {"rice":60,"sugar":40,"maggie":40,"cologate":90,"panner":110,"salt":20,"boost":90,"oil":160}

option = int(input("For list of items press 1 are 2 for exit:"))
if option == 1:
    print(list_items)
for i in range(len(items)):
    option = int(input("If you want to buy press 1 are 2 for exit:"))
    if option == 2:
        break
    elif option == 1:
        item = input("enter your item:")
        quantity = int(input("enter your quantity:"))
        if item in items.keys():
            price = quantity * (items[item])
            price_list.append((item,quantity,price))
            total_price += price
            gst = total_price*5/100
            final_amount = gst+total_price
            item_list.append(item)
            quantity_list.append(quantity)
            p_list.append(total_price)
        else:
            print("soory you are item is not available")
    else:
        print("you entered a wrong number")
    option = input("if you want to print a bill press yes or no:")
    if option == "yes" or option == "Yes":
        pass
        if final_amount != 0:
            print(25*"=","sri sai kiran super market",25*"=")
            print(33*"=","wanaparthy",33*"=")
            print("Name:",name,32*" ","Date:",datetime.now())
            print(78*"-")
            print("Sno",10*" ","item",10*" ","quantity",10*" ","price",10*" ")
            for i in range(len(price_list)):
                print(i,12*" ",item_list[i],12*" ",quantity_list[i],16*" ",p_list[i],10*" ")
            print(78*"-")
            print(50*" ","Totalamount","Rs:",total_price)
            print(50*" ","gst amount ","Rs:",gst)
            print(78*"-")
            print(50*" ","FinalAmount","Rs:",final_amount)
            print(78*"-")
            print(25*"=","Thanks For Visiting",28*"=")
            print(78*"=")
            
            




    
        




        