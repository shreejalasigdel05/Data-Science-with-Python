import numpy as np

# arr=np.array([10,20,30,40,50])
# print(arr)
# print(arr[1])
# print(arr[-1])
# arr2=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr2[1][2])
# print(arr2[0][1])

# arr=np.array([10,20,30,40,50])
# print(arr[2:4])
# print(arr[1:])
# print(arr[::-1])

# arr2=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr2[:2,:2])
# print(arr2[1:3,0:3])

# arr=np.array([1,2,3,4,5,6])
# arr_new=arr.reshape(2,3)
# print(arr_new)
# print(arr_new.ndim)

# arr_2d=np.array([[1,2,3],[4,5,6]])
# print(arr_2d.ndim)

# arr_3d_a=np.expand_dims(arr_2d,axis=0)
# print(arr_3d_a)

# arr3d=arr_2d.reshape(1,2,3)
# arr3d=arr_2d.reshape(1,3,2)
# print(arr3d)

# arr=np.arange(12)
# print(arr.ndim)
# new_arr=arr.reshape(2,3,2)
# print(new_arr.ndim)
# print(new_arr[0])
# print(new_arr[1])

arr_3d=np.arange(24).reshape(3,2,4)
print(f'3d shaped{arr_3d.ndim}')
print(arr_3d)

