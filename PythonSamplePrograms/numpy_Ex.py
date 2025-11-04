import numpy as np

npDs=np.array([[[1,2,3],[4,5,6]],[[11,12,13],[14,15,16]]])
print("Numpy array is :{}".format(npDs))
print("Type of Numpy array is :{}".format(type(npDs)))

print("Length is {}".format(len(npDs)))
print("Dimension is {}".format(npDs.ndim))

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print("A :{}".format(a.ndim))
print("B : {}".format(b.ndim))
print("C :{}".format(c.ndim))
print("D : {}".format(d.ndim))

npDS=np.array([1,2,3,4,5],ndmin=5)
print(f"Number of dimensions in the array : {npDS.ndim}")

#selecting an element in 1 Dimnesion Array
arr=np.array([1,2,3,4,5,6,7,8])
print(f"Fourth element of array : {arr[3]}")
print("Selecting all elements of array starting with 5th item", arr[4:])
print("Negative Slicing of Array",arr[-3:-1])
print("Using Step function",arr[1:5:2])

#selecting elements in 3D array
npDs3=np.array([[[1,2,3],[4,5,6]],[[11,12,13],[14,15,16]]])
print(f"Selecting single element of 3D array : {npDs3[1,0,2]}")
print(f"Selecting Multiple elements of 3D array : {npDs3[1,0,1:]}")
print(f"Selecting Multiple elements from Multiple dimensions of 3D array : {npDs3[1,0:,1:]}")

#Converting Datatypes - Float to integer
arr1=np.array([[[1.2,2.4,3],[4,5.7,6]],[[11.2,12,13.6],[14.9,15,16.4]]])
arr2=arr1.astype(int)
print(f"Array Before changing to Int: {arr1}")
print(f"Array After changing to Int: {arr2}")

#Converting Numerical array to Boolean : 0 becomes False, everything else becomes True
arr = np.array([-1.5,-2,1, 0, 2,3,4,5])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)

#Copying and Viewing array. Changes to original array or view array will reflect in both arrays but not copied array
arr = np.array([-1.5,-2,1, 0, 2,3,4,5])
newArrC=arr.copy()
newArrV=arr.view()
arr[4]=100
newArrV[6]=200
print("Output of Copied Array",newArrC)
print("Output of Viewed Array",newArrV)
print("Output of Original Array",arr)

#Finding the Shape of the array and Reshaping the array
npDs3=np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])
print(f"Shape of the Array is : {npDs3.shape} and Dimension of input array is : {npDs3.ndim}")
npDS4=npDs3.reshape(2,2,2,2)
print(f"Array after Reshaping is : {npDS4} and Dimension of new Array is {npDS4.ndim}")
npDs4=npDs3.reshape(-1)
print(f"Flattended Array is : {npDs4}")

#Iterating through Arrays : For Loop , loops through n-1 Dimension
arr=np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])
for x in arr:
    print("Element to be printed in 1st For Loop is :",x)
for x in arr:
    for y in x:
        print(x, "Element to be Printed in 2nd For Loop is: ",y)

#Functions on Arrays : Concatenate, sort and  Search
arr=np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])
indOfArr=np.where(arr==12)
print(f"Index of selected item in the array is : {indOfArr})

#Concatenating Arrays
arr1=np.array([1,2,3,4])
arr2=np.array([11,12,13,14])
arr3=np.array([21,22,23,24])
mergArray=np.concatenate((arr1,arr2,arr3))
print(f"Merged/Concatenated Array is : {mergArray}")

#concatenating Arrays with more than 1 Dimension using Axis=0 or 1
arr11=np.array([[1,2,3,4],[5,6,7,8]])
arr21=np.array([[11,12,13,14],[15,16,17,18]])
mergeArr2D=np.concatenate((arr11,arr21), axis=0)
print(f"Merged 2D Array with Axis 0 : {mergeArr2D}")
print(f"Dimension of Merged Array with Axis 0: {mergeArr2D.ndim} and shape is {mergeArr2D.shape}")
mergeArr2D=np.concatenate((arr11,arr21), axis=1)
print(f"Merged 2D Array with Axis 1 : {mergeArr2D}")
print(f"Dimension of Merged Array with Axis 1: {mergeArr2D.ndim} and shape is {mergeArr2D.shape}")


#Stacking  - Stacking adds new dimension to Arrays

arr11=np.array([[1,2,3,4],[5,6,7,8]])
arr21=np.array([[11,12,13,14],[15,16,17,18]])

mergArray2=np.stack((arr11,arr21), axis=0)
print(f"Dimension of Stacked Array with Axis 0 is : {mergArray2.ndim} and Shape is {mergArray2.shape}")
print(f"Stacked/Merged/concatenate Array with Axis=0 is : {mergArray2}")


mergArray3=np.stack((arr11,arr21), axis=1)
print(f"Dimension of Stacked Array with Axis 1 is : {mergArray3.ndim} and Shape is : {mergArray3.shape}")
print(f"Stacked/Merged/concatenate Array with Axis=1 is : {mergArray3}")

#sorting numpy arrays
arr11=np.array([[1,22,9,5],[11,19,8,6]])

arrSort=np.sort(arr11,axis=1)
print(f"Sorted Array with Axis 1 : {arrSort}")

arrSort=np.sort(arr11,axis=0)
print(f"Sorted Array with Axis 0 : {arrSort}")

#Additiona and Multiplication of Arrays
arr2=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
arr3=np.array([5,6,7,8,9,10,11,12,13,14,15,16])

addArr=arr2 + arr3
print(f"Addition of Arrays : {addArr}")
multArr=arr2 * arr3
print(f"Multiplication of Arrays {multArr}")

#Multiplication by leveraging numpy Package
multnpArr=np.multiply(arr2,arr3)
print(f"Multiplication of Arrays using numpy package {multnpArr}")

#Multiplication of Multi Dimension Arrays
arr1=np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])
arr2=np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])
multnp=np.multiply(arr1,arr2)
print(f"Multiplication of Arrays using numpy package {multnp}")

multarr=arr1*arr2
print(f"Multiplication of Arrays : {multarr}")

#Creating Universal Function for using Vecorization for compuation.
#frompyfunc() - Function is used to convert a user defined function into Universal Function

def myNpFunc(arr1,arr2):
    arr3=np.add(arr1,arr2)
    arr4=arr3*10
    return arr4

arr_1=np.array([[10,11,12,13,14,15],[1,2,3,4,5,6]])
arr_2=np.array([21,22,23,24,25,26])
myResult=myNpFunc(arr_1,arr_2)
print(myResult)

myfromPyFunc=np.frompyfunc(myNpFunc,2,1)

print(myfromPyFunc([2,3,4],[5,6,7]))

