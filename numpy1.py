import numpy as np

# li={1,2,3,4,5}
# arr=np.array([10,20,30,40])
# print(type(li))
# print(type(arr))
# print(arr)
# print(len(arr))
# for i in arr:
#     print(i)

arr=np.arange(0,5,1)
# print(arr)
# print(arr.shape)
# print(arr.ndim)
# print(arr.size)
# print(arr.dtype)

#aggregate fns
s=np.sum(arr)
print(s)
print(np.max(arr))
print(np.mean(arr))
print(np.std(arr))

for i in arr:
    print(i)