class Tax:
    def __init__(self,name,rate):
        self.name=name
        self.rate=rate
        print("Adding line :Third change ")

    def computeTax(self,income,age):
        print(f"Tax Computation for:{self.name}")
        if age<60:
            tax=income*self.rate
        else :
            tax=income*self.rate/2
        return tax

    def taxFunc(self,tax):
        return lambda x: x * tax

    print("Adding line :Second change ")

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

print("Adding line :First change ")

taxCompute=Tax("Saachi & Saanvi",0.5)
taxPay=taxCompute.computeTax(1000,45)
print(f"Tax to be paid by {taxCompute.name} is : {taxPay}")

listName=["Sanath","Satheesh","Ishaank","Saraswathi"]
listInc=[1000,2500,5000,25000]
listAge=[45,75,13,61]
i=-1
for item in listName:
    taxCompute=Tax(item,0.4)
    i=i+1
    taxPay=taxCompute.computeTax(listInc[i],listAge[i])
    print(f"Tax to be paid by {item} is : {taxPay}")




