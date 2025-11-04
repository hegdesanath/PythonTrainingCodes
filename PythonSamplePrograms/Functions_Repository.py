#Example of running calling a function with arguments (positional and Keyword) and use of try except Block
def computeTax(income,age,rate):
    if age<60:
        tax=income*rate
    else :
        tax=income*rate/(age-60)
    return tax

#Passing a dictionary to function and accessing elements in the dictrionary
def printDetails(mydict):
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


def taxFunc(tax):
    return lambda x:x*tax