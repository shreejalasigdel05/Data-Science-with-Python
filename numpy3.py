import numpy as np
#indexing,slicing,reshaping
# arr=np.array([10,20,30,40,50])
# print(arr)
# print(arr[0])
# print(arr[1])

# arr2=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr2)

#access individual element
# print(arr2[1][2])

#slicing
# arr=np.array([10,20,30,40,50])
# print(arr[1:4])
# print(arr[:3])
# print(arr[2:])
# print(arr[::2])
# print(arr[::-1])

#2D slicing
# b=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(b.ndim)
# print(b[:2,:2])
# print(b[:3,:2])
# print(b[0,:])
# print(b[:,1])
# print(b[:,2])

#reshaping
# arr=np.array([1,2,3,4,5,6])
# print(arr.ndim)
# b=arr.reshape(2,3)
# print(b)
# print(b.ndim)
# na=arr.reshape(3,2)
# print(na)

#2D to 3D
# b=np.array([[1,2,3],[4,5,6]])
# print(b.shape)
# a=b.reshape(1,3,2)
# print(a)
# print(a.ndim)


# arr=np.arange(12)
# print(arr)
# print(arr.ndim)
# arr2=arr.reshape(4,3)
# print(arr2)
# arr1=arr.reshape(12,1)
# print(arr1)
# arr3=arr.reshape(6,2)
# print(arr3)
# arr4=arr.reshape(2,2,3)
# print(arr4)

arr=np.arange(1,13)
arr2=arr.reshape(3,4)
print(arr2)
print(arr2[1])
print()
