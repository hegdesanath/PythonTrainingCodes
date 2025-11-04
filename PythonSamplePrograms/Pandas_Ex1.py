
import pandas as pd

#Create Pandas DataFrame from List
list = [["Sanath", 45, "Korba"],
    ["Ishaank", 13, "Bangalore"],
    ["Ishaanya",  12, "Whitefield"]
        ]
dataList=pd.DataFrame(list,columns=['Name','age','Place'])
print(dataList.head(3))

#Create Pandas DataFrame from Dictionary
dict = { "Name":["Sanath","Ishaank","Ishaanya","Saraswathi"],
         "Age": [45,13,12,72],
         "Place":["Korba","Bangalore","Whitefield","NGEF"]
         }
dataDict=pd.DataFrame(dict,columns=['Name','Age','Place'])
print(dataDict.head())

#Reading CSV File
df=pd.read_csv("C:\\Users\\sanat\\PycharmProjects\\PythonProject\\Datasets\\MobilePriceClassificationDataset\\train.csv")

#Basic Functions used in pandas
print(df.head())
print(df.info())
print(df.dtypes)
print(df.shape)

print(df.describe())
descDf=df.describe(percentiles=[0.2, 0.4, 0.6,0.8], include=[int, float])
#Output dataframe to a CSV file
descDf.to_csv("describeOutput.csv", index=True)

#To print the entire Dataframe : All Columns and rows are printed, unlike head
print(df.to_string())


for i in range(0,len(df)):
    df.loc[:1000,"CHAR_VAR"]="ABCD"
    df.loc[1001:,"CHAR_VAR"]="DEFA"
    df.loc[:1000,"Name"]="INDIA"
    df.loc[1001:,"Name"]="SANATH"

#print(df.to_string())
#Sort values by multiple variables
df.sort_values(by=["mobile_wt","pc"],inplace=True)
df.sort_index(inplace=True)#dataframe goes back to the order in which it read the file
df.sort_values(by="px_height", ascending=False, inplace=True)

# Applying String Function on a column of DataFrame
df["CHAR_VAR"]=df["CHAR_VAR"].str.lower()
#Applying multiple String functions at Once
df["CHAR_VAR"]=df["CHAR_VAR"].str.upper().str.replace("A","XX")

#Finding the frequency count of categorical / Numerical values
print(df["px_height"].value_counts())
#Reseting the index of the dataframe if the index  has changed after multiple data manipulation operations
df.reset_index(inplace=True, drop=True)#without drop=True, existing Index gets added as a column

#Applying lambda function on a column
df["Name"]=df["Name"].apply(lambda x:x.replace("A","XX"))
testXl1["m_dep"]=testXl1["m_dep"].apply(lambda x: round(x))
#print(df.to_string())

# Convert a column into integer datatype from string
testXl1["m_dep"]=testXl1["m_dep"].astype(int) #converts a column having  numeric values to int

df.rename(columns={"mobile_wt":"MOBILEWEIGHT", "px_height":"PXHEIGHT"}, inplace=True)
dfPrint=df.loc[:5,:]

#Using .loc to i) change all values in a Column to 100, ii) change all values in first 2 Rows to 999
# iii) change All values in 3 columns to 3333  iv) change the variable type from float and char to int
dfPrint.loc[:,"int_memory"]=100
dfPrint.loc[:1,:]=999
dfPrint.loc[:,["price_range","CHAR_VAR","Name"]]=3333
dfPrint[["clock_speed","CHAR_VAR","Name"]]=dfPrint[["clock_speed","CHAR_VAR","Name"]].astype(int)
print(dfPrint.to_string())
print(dfPrint.info())

testXl1=testXl.loc[:10,:]
trainXl1=trainXl.loc[:13,:]
#concatenate/Join 2 dataframes Next to each other -
# axis=0 Appends(one below other) data, and axis=1, joins the data (side by side) by index values
# Ignore_index=True creates a new index starting from 1. For columns, column names are replaced with 0 to n
ds=pd.concat([trainXl1,testXl1],ignore_index=True, axis=0)
print(ds.to_string())

#Creating an ID variable for trainXl dataFrame
i=0
for i in range(0,len(trainXl1)):
    trainXl1.loc[i,"id"]=i+1

#Concatenate to append 1 dataset to another , axis=0 to indicate, dataset one below other
test_inter=testXl.loc[15:20,:]
testNew=pd.concat([testXl1, test_inter], axis=1)
#print(testNew.to_string())

#Join 2 Data frames based on Key : Inner Join
train_new=pd.merge(trainXl1,testNew, on="id", how="inner")
#print(train_new.to_string())
#Join 2 Data frames based on Key : Right Join
train_new=pd.merge(trainXl1,testNew, on="id", how="right")
print(train_new.to_string())

import pandas as pd
# To Avoid - SettingWithCopyWarning: A value is trying to be set on a copy of a slice from a DataFrame
pd.options.mode.copy_on_write = True

testXl=pd.read_excel("C:\\Users\\sanat\\PycharmProjects\\PythonProject\\Datasets\\MobilePriceClassificationDataset\\PDtest.xlsx")
testNew=testXl.loc[:10,]
testNew.loc[:1,"mobile_wt"]=None
testNew.loc[:3,"clock_speed"]=None

#Used to fill missing values for numeric variable. Mean or other functions can be used.
#To apply mean function for missing values for all variables
testNew.loc[:,:]=testNew.fillna(testNew.mean())
#To apply mean function for missing values for 2 variables
testNew.loc[:,["mobile_wt","clock_speed"]]=testNew[["mobile_wt","clock_speed"]].fillna(testNew.mean())

#use of apply function on a dataframe variable
testNew.loc[:,"mobile_wt"]=testNew["mobile_wt"].apply(lambda x: round(x,2))


testNew=testXl.loc[:10,]
testNew.loc[:1,"mobile_wt"]=None
testNew.loc[:2,"clock_speed"]=None
testNew.loc[:3,"int_memory"]=None
testNew.loc[:4,"n_cores"]=None

#Removes the Row from the data frame if any of the variable in the row has missing value
testNew.dropna( how="any",axis=0,inplace=True)
print(testNew.shape)
#Removes the Column from the data frame if all of the values in the column has missing value
testNew.dropna( how="all",axis=1,inplace=True)
#Removes the Column from the data frame if count of non missing data in column under consideration
# is less the value mentioned in thresh
testNew.dropna( thresh=8,axis=1,inplace=True)
print(testNew.shape)
print(testNew.to_string())

#Dropping columns in a dataframe
testNew.drop(columns=["battery_power","mobile_wt","clock_speed","int_memory","n_cores"], axis=1, inplace=True)

#Compare 2 Dataframes to check similarity or difference between 2  Dataframes.
# Both Dataframe should have same number of records (rows and columns), otherwise there will be an error
testNew=testXl.loc[:10,]
testCp=testNew.copy()
testNew.loc[:1,"mobile_wt"]=7
testNew.loc[:2,"clock_speed"]=8
testNew.loc[:3,"int_memory"]=9
testNew.loc[:4,"n_cores"]=10
n1=testNew.compare(testCp,keep_shape=False, keep_equal=False, align_axis=1)
print(n1.to_string())

#Strippping leading and trailing blanks: lstrip() for leading blanks and rstrip() for trailing blanks
testNew=testXl.loc[:10,]
for i in range(0,len(testNew)):
    if i % 2 == 0: testNew.loc[i,"NewCat"]="A B C"
    else: testNew.loc[i,"NewCat"]="  A B C  "
testNew["NewCat"]=testNew["NewCat"].str.strip()
print(testNew.to_string())

#Grouping data in Pandas :
# Multiple variables can be selected for Grouping but only 1 Groupby variable can be selected
testGroup=testNew[["int_memory","four_g","m_dep","mobile_wt"]].groupby(testNew["touch_screen"])
print(testGroup.head())
meanGroup=testGroup.mean().round(3)
print(meanGroup)
meanGroupA=meanGroup.apply(lambda x: x+100)
print(meanGroupA.head())

# iterrows() returns 2 values - Row number and an array of data in the row
for i, row in testNew.iterrows():
    testNew.loc[i,"DateF"]=pd.Timestamp('2023-10-04 15:30:00')
    testNew.loc[i,"New_Field"]=row["battery_power"]+5*i
    # All Rows in the column are overwritten with last value (max row count) which i takes
    testNew["newID"] = i
    # All Rows in the column are assigned with last value present in the dataframe for variable "battery_Power"
    testNew["newBatter_Power"] = row["battery_power"]

#Example of using Date time Functions
testNew["OnlyYear"]=testNew["DateF"].dt.year
testNew["OnlyTime"]=testNew["DateF"].dt.time
testNew.drop(columns={"blue","clock_speed","dual_sim","fc","four_g","int_memory","m_dep","mobile_wt","n_cores","pc","px_height","px_width","ram"}, inplace=True)
print(testNew.to_string())
