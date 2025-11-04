
#Example of running calling a function with arguments (positional and Keyword) and use of try except Block
def computeTax(income,age,rate):
    if age<60:
        tax=income*rate
    else :
        tax=income*rate/(age-60)
    return tax


try:
    income=int(input("Enter Income"))
    age=int(input("Enter Age"))
    print("Tax to be paid is :{}".format(computeTax(income,age,0.5)))
except ZeroDivisionError:
    print("Do Not enter Age=60")
except Exception as e:
    print("Error is ",e)
finally:
    print("Program run completed")


#Passing a dictionary to function and accessing elements in the dictrionary
def printDetails(mydict):
    print("Key is : ",mydict.keys()," value is :",mydict.values())
    for key in mydict.keys():
        print("Key is : ", key," Value is : ", mydict[key])
    return

dictDef = {"Name": "Sanath", "age":45, "income":100}
printDetails(dictDef)

#*argNames is used to define unknown number of positional arguments
#**kwargNames is used to define unknown number of Keyword Arguments (arguments having a predefined name)
def kwargsex(*argNames,**kwargNames):
    i=len(argNames)
    c=0
    print("Length of variable Names is : ",i )
    for j in argNames:
        c=c+1
        print(c," Positional Variable Value is :",j)
    for key in kwargNames.keys():
        print("Key is : ",key," and Value is : ",kwargNames[key])
    return

listName=["Sanath","Hegde","Ishaank","Ishaanya"]
DictName={"Name":"Sanath","age":45,"income":100,"Location":"Bangalore"}
#*names is used to unpack a list having name listName
#**DictName is used to unpact a Dictionary having name DictName
kwargsex(*listName,**DictName)


#Examples of using Lambda Function
#Also Examples of Map, Sorted and Filter functions
numbers=[4,1,8,3,10,2,6,14]
print(numbers)
newNumber=sorted(numbers)
print(newNumber)

MultiplyNumber= lambda x:x*5
print(f"Applying a Lambda function to multiply a number by 5 is : {MultiplyNumber(2)}")
#Map is used to apply a function on a List or a Dictionary
lambdaNum=list(map(lambda x:x*7, numbers))
print(f"Applying Lambda function to multiply by 7 is : {lambdaNum}")

def taxFunc(tax):
    return lambda x:x*tax

income=int(input("Enter the income:"))
taxtoPay=taxFunc(tax=0.3)
print("Tax to be paid is : ",taxtoPay(income))

print("testing git hub on Functions_Ex file")