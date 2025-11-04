import datetime as dt
import pandas as pd
import numpy as np

#Program to take input value for Birthday and calculate age.
#Program demostrates working with datetime functions using datetime package
#Demostrates usage of pandas dataframe with basic operations on dataframe

try:
    name = input("whats your name")
    birthDate = input("enter your birth date in dd/mm/yyyy format")
    print(dt.datetime.strptime(birthDate,"%d/%m/%Y"))
    age=(dt.datetime.today().year - dt.datetime.strptime(birthDate,"%d/%m/%Y").year)
    print(age)
    print("Hi "+ name + " Your age as of "+ str(dt.datetime.now().date()) +" is " + str(age))
    todayDt=dt.datetime(dt.datetime.now().year,dt.datetime.now().month , dt.datetime.now().day)
    data=[[name,dt.datetime.strptime(birthDate,'%d/%m/%Y'),todayDt]]
    df=pd.DataFrame(data, columns=["name","birthDate","today"] )
    df['age']=[age]
    print(df.dtypes)
    print(df)
    df['newage']=((df['today']-df['birthDate']).dt.days)/365
    df['newage']=df['newage'].apply(lambda x: np.floor(x))
    print(df)
except ValueError:
    print("something went wrong:{ValueError}")
except Exception as e:
    print("Date was not given in in proper format : " + str(e))
