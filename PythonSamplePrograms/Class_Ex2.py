class Tax:
    def __init__(self,name,rate):
        self.name=name
        self.rate=rate
    def computeTax(self,income,age,rate):
        #print(f"Tax Computation for:{self.name}")
        if age<60:
            tax=income*rate
        else :
            tax=income*rate/2
        return tax

    def taxFunc(self,tax):
        return lambda x: x * tax

    #Passing a dictionary to function and accessing elements in the dictrionary
    def printDict(self, mydict):
        print("Key is : ",mydict.keys()," value is :",mydict.values())
        for key in mydict.keys():
            print("Key is : ", key," Value is : ", mydict[key])
        return

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

#Example of one class Extending(Inheritance) from Another class
class AllTax(Tax):
    def __init__(self,name, rate):
        self.name=name
        self.rate=rate
    def nriTax(self,income,age,rate):
        #print(f"NRI Tax Computation for:{self.name}")
        tax=Tax(self.name, self.rate).computeTax(income, age, rate)
        return tax




listName=["Sanath","Satheesh","Ishaank","Saraswathi"]
listInc=[1000,2500,1000,2500]
listAge=[45,75,13,61]
listDomicile=["NRI","IND","IND","NRI"]
i=-1
for item in listName:
    i=i+1
    if listDomicile[i]=="NRI":
        taxCompute=AllTax(item, 0.5)
        taxPay = taxCompute.nriTax(listInc[i],listAge[i],0.25)
        #print(f"NRI Tax to be paid by {item} is : {taxPay}")
    else:
        taxCompute=Tax(item,0.4)
        taxPay=taxCompute.computeTax(listInc[i],listAge[i],0.2)
        #print(f"Tax to be paid by {item} is : {taxPay}")

simpleTax=AllTax("Saurabh",0.2).taxFunc(0.7)
#print(f"Simple Tax Calculation is : {simpleTax(10000)}")

import random
class Dice:
    def roll(self):
        return (random.randint(1,6),random.randint(1,6))

print("testing class Ex2 change")