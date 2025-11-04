import math
import random

#Usage of basic mathematical funtions
comp=20//3
print(f"Division of 10 by 3 and removing decimals or Floor : {comp}")
mathfun=math.ceil(10/3)
print(f"Division of 10 by 3 and rounding to higher integer is : {mathfun}")

#Usage of if loops
creditHistory="Good"
criminalHistory=False
income=9000
if creditHistory.upper()=="GOOD" and not criminalHistory and income>=10000:
    print("Loan can be given")
elif criminalHistory==True:
    print("Loan cannot be given")
elif creditHistory.upper()=="GOOD":
    print("Collateral is required")
else:
    print("Loan to be reviewed by credit team  ")

while (income<20000):
    print("Income is {} which is less than 20000".format(income))
    income=income+5000
print("Income when coming out of loop criteria is satisfied is ",income)

#Usage of While loop
secretNumber=random.randint(1,5)
guessLimit=3
guessCount=0
while (guessCount<guessLimit):
    guess=int(input("Enter your Guess"))
    if guess==secretNumber:
        print("You guessed correctly")
        break
    else :
        guessCount=guessCount+1
else:
    print("You exhausted your chances. Secret Number =",secretNumber)

#use of Zip Function
product = ['apple', 'banana', 'orange', 'grape']
price = [100, 50, 200, 300]
quantity = [1, 2, 3, 4]
dict={"Sanath":45, "Ishaank":13, "Ishaanya":12, "Saraswathi":62, "Satheesh":78}
tup1=(100,"Korba",200,"bangalore",300)

#Creating a 2-D List using zip Function by passing multiple lists
newList=list(zip(product,price,quantity))
print(f"New List created using zip  Function is {newList}")
print(f"Type of newList is : {type(newList)}")

#Unpacking of a list into multiple individual list using *zip
upackedProduct, unpackedPrice, unpackedQuantity = zip(*newList)
print(f"Unpacked Product List : {upackedProduct}, Price List : {unpackedPrice} and "
      f"unpacked Quantity List : {unpackedQuantity} created using *zip  Function ")
print("Type of unpackedProduct is : {}".format(type(upackedProduct)))

#converting a Dictionary into 2 separate list for keys and values using zip Function
dKey=list(dict.keys())
dVal=list(dict.values())
print(f"List containing only the Keys in Dictionary is  {dKey}")
print(f"List containing only the Values in Dictionary is  {dVal}")
print("Type of dKey is : {}".format(type(dKey)))

#Using a map Function on a List
mapR=list(map(lambda x: x*5, price ))
print("Multiplying all values in a list: {} by 5 and output is {}".format(price,mapR))
#Using a map Function by providing two lists as input
mapCost=list(map(lambda x,y : x*y, price,quantity ))
print("Total Cost : Multiplying Price: {} by Quantity {} and output is {}".format(price,quantity,mapCost))
mapShip=list(map(lambda x,y : x*y*0.2, price,quantity ))
print("Shipping Cost : Multiplying Price: {} by Quantity: {} and 0.2 output is {}".format(price,quantity, mapShip))

#Examples of  using Sorting function on List and Dictionary
priceS=sorted(price)
print(f"Sorted price is: {priceS}")
price.sort(reverse=True)
print(f"Sorted price is: {price}")
#Sorting on Dictionary items leads to sorting on Keys of Dictionary
dictS=sorted(dict.items())
print(f"Sorted Dictionary is: {dictS}")

#Applying Filter function on a List
product = ['apple', 'banana', 'orange', 'grape','Apple']
price = [100, 50, 200, 300,10000]
FilterPrice=list(filter((lambda x:x>100),price))
print(f"After Applying filter on the Price List : {FilterPrice}")
FilterProduct=list(filter((lambda x:x.lower()=="apple"),product))
print(f"After Applying filter on the Product List : {FilterProduct}")

#Example of using Sets - Sets can have only unique values (unlike lists). Duplicates will be ignored.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
tup1=(11,12,13)
l1=[100,200,300,400]

myset = set1.union(tup1)
print(myset)
myset3=myset.union(set2,set3,set4,l1)
print(f"Union of Set, Tuple and List is : {myset3}")
