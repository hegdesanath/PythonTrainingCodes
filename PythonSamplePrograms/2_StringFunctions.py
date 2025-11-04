
#Working with Strings

string = [3,89,23,76,5,50,2,67]
string.append(234)
print(f"Append Function : {string}")
print(f"Index function : {string.index(23)}")
string.insert(3,100)
print("String after inserting is : {}".format(string))
string.remove(string.index(5))
print("String after removing is : {}".format(string))
string.sort()
print("String after sorting in Ascending order is : {}".format(string))
string.reverse()
print("String after sorting in Descending order is : {}".format(string))
string.pop(2)
print("String after popping is : {}".format(string))

course="Python Beginner cOurse"
strLen=len(course)
print("Output 1 Length of String '",course , "' is : " + str(strLen))
newStr2=course[:strLen-5]
print("output2 : Length is: {} and newStr2 is {}: ".format(strLen,newStr2))
print(f"output 3: {course[7:10]} having length of {strLen} end of statsement")
print("Output 4: ",course[-5:-1])

print("Location of 'O' in the string course is : ",course.find("O"))
print("Location of 'o' in the string course is : ",course.find("o"))
print("Location of 'T' in the string course is : ",course.find("T"))
print("Location of 'T' in the string course after capitalization is : ",course.upper().find("T"))
print("String Replacement fuction : ", course.replace ("Beginner","Starter"))

#Basic For Loop using Range function
strCnt=3
endCnt=7
for i in range(strCnt,endCnt):
    print("*"*i,"#"*(i-1))
    print(f"value of i  is : {i}")

#Program for iterating through Lists and performing operations on list
product = ['apple', 'banana', 'orange', 'grape']
price = [100, 50, 200, 300]
quantity = [1, 2, 3, 4]
cost=[]
totalCost=0
for i in range(len(product)):
    cost.append(price[i] * quantity[i])
    print(f"Cost of {product[i]} is {cost[i]}")
    totalCost+=cost[i]
print(f"Total Cost of all items is {totalCost}")

#Forloop and Multidimension lists : Creating a list and appending values to the list through Program
x=[]
for i in range(4):
    x.append((i+3,i*5,i*10))
print(x)

#Nested For loop along on Multi Dimension List : Printing all elements in a List along with its position
x=[["ABC","DEF","GHI"],["JKL","MNO","PQR"],["TUV","WXY","ZAB"]]
print(x[2][2])
i=0
j=0
for item1 in x:
    i+=1
    j=0
    for item2 in item1:
        j+=1
        print(f"Item in {i} list, and {j} Sublist is : ",item2)

#Program for Finding the largest number in a list
import random
x=[]
size=random.randint(1,20)
print(size)
for i in range(size):
    x.append((random.randint(1,100)))
print (x)
largest=x[0]
position=0
for item in x:
    if item>largest:
        largest=item
        position=x.index(item)
print (f"Largest number in the list is {largest} at position {position+1}")

#Remove Duplicates from a string
#Method 1
string=[10,12,5,26,2,5,19,12,15,9,5,9]
stringcp=[]
i=0
for item in string:
    i=i+1
    itemMatch=0
    for item2 in string[i:]:
        if item2==item:
            itemMatch=1
            break
    if itemMatch==0:
        stringcp.append(item)
print(stringcp)

#Remove Duplicates from a string
#Method 2
string=[10,12,5,26,2,5,19,12,15,9,5,9,19,10,26]
string.sort()
print(string)
stringcp=[]
i=-1
for item in string:
    i=i+1
    if i==0:
        stringcp.append(item)
        continue
    if item!=string[i-1]:
        stringcp.append(item)
print(f"New String after removing duplicates is {stringcp}")

#Remove Duplicates from a string
#Method 3
string=[10,12,5,26,2,5,19,12,15,9,5,9,19,10,26]
stringcp=[]
for numbers in string:
    if numbers not in stringcp:
        stringcp.append(numbers)
print(f"New String after removing duplicates is {stringcp}")

#Tuples are immutable. They have only 2 functions : Count and Index.
# Used when we do not want values to be changed at any stage of the program.
tupleSamp=(34,56,84,12,100,84,56,45,56,10)
print(f"Example of using index function on Tuple and returning a value is : {tupleSamp.index(56)}")
tupLen= len(tupleSamp)
print(f"Example to count number of items in the Tuple : {tupLen}")
tupCnt= tupleSamp.count(56)
print(f"Example of using Count function on Tuple to frequency of an item in the Tuple : {tupCnt}")

#Example of using a tuple : Tuple can have multiple data types - str, int float and is immutable
# Tuple can have Duplicates. hence count() function is used to count number of items with specific value
# Although Tuple is immutable, if you reassign the Tuple with a new tuple, it will allow it
# contd...since it is recreating a new Tuple
tupEx=("Sanath",45,"AGM",100000,"AGM")
print(type(tupEx))
tupEx=tupEx + ("Ishaank","Ishaanya")
print(tupEx)
tupEx=tupEx + ("Daddy",)
print(tupEx)

#Example of Unpacking - Works on both Lists and Tuples
stringSample=(34,56,84)
s1, s2, s3=stringSample
print (f"First String is : {s1} ; Second String is : {s2} and Third String is : {s3}")

#Example of Dictionary
sampDict = {
    1:"ONE",
    2:"TWO",
    3:"THREE",
    4:"FOUR",
    5:"FIVE",
    6:"SIX",
    7:"SEVEN",
    8:"EIGHT",
    0:"ZERO"
}
inputNum=input("Input a number")
output=""
for num in inputNum:
    output=output + sampDict.get(int(num),"<NA>") + " "
print(output)

#Replace certain words/characters in a string with pre-defined Dictionary key, value pairs
sampDict = {
    "*":"STAR",
    "#":"HASH",
    "!":"EXCLAMATION",
    "?":"QUESTION"
}
inputNum=input("Input a Sentence")
wordList=inputNum.split(" ")
output=""
for word in wordList:
    output=output + sampDict.get(word,word) + " "
print(output)

#Using Inspect Package to see the source code of functions/classes/Pacakges
import inspect
import PythonSamplePrograms.Class_Ex2 as sp
print(inspect.getsource(sp.AllTax.kwargsex))

#final decorator can be used to declare a variable or class or function as Final
#However, if you override a final variable/Function/Class there will not be a run time error
#Only the IDE's such as Pycharm show a warning to inform programmer not to edit, but it is not a mandate
from typing import final
var1: final = 100
print(f"Initially assigned value for var1 is {var1}")
var1=300
print(f"Value in var1 after reassignment is {var1}")
