import pandas as pd
itemNo=int(input("Enter the number of item you want to buy"))
itemName=[]
itemPrice=[]
Quantity=[]
Amount=[]
for i in  range(0,itemNo):
    Name_of_item=input("Enter the item name")
    itemName.append(Name_of_item)
    Price_of_item=float(input("Enter the price of the item"))
    itemPrice.append(Price_of_item)
    
    quantity =int(input("Enter the quantity"))
    Quantity.append(quantity)
    amount=Amount.append(quantity*Price_of_item)
df=pd.DataFrame({"Name":itemName,"Price":itemPrice,"Quantity":Quantity,"Amount":Amount})
print(df)