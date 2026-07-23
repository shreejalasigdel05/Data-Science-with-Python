import numpy as np
# arr=np.array([10,20,30,40])
# print(arr)
# print(np.add(arr,5))

# print(np.subtract(arr,3))
# print(arr-3)

# print(np.multiply(arr,2))

# print(np.divide(arr,10))

# arr=np.array([9,5,10,20,30,40])

# print(arr//2) #quotient
# print(arr%2) #reminder
# print(arr**2) #power

# arr=np.array([9,10,20,30,40,50])
# print(np.sqrt(arr)) #square root
# print(np.square(arr)) #square
# print(np.exp(arr)) #exponential 

# arr=np.array([-5,10,-15])
# print(np.abs(arr)) #modulo (+->- and -->+)

# prices=np.array([10.40,20.60,31.90,55.20])
# print(np.round(prices).astype(int))
# print(np.round(prices))

# angles=np.array([0,np.pi/2,np.pi])
# print(np.sin(angles))
# print(np.cos(angles))
# print(np.tan(angles))

# arr=np.array([10,20,30,40,50])
# print(np.mean(arr))
# print(np.median(arr))
# print(np.std(arr))
# print(np.var(arr))
# print(np.min(arr))
# print(np.max(arr))

# print(np.max(arr)-np.min(arr))

# arr=np.array([1,10,100])
# print(np.log(arr))
# print(np.log10(arr))
# print(np.log2(arr))

# arr=np.array([2.3456,5.6789])
# print(np.round(arr,2))
# print(np.floor(arr).astype(int))
# print(np.ceil(arr))

# arr=np.array([[10,20,30],[40,50,60]])
# print(np.sum(arr))
# print(np.sum(arr,axis= 1)) #row wise
# print(np.sum(arr,axis= 0)) #column wise
 
# print(np.mean(arr, axis=1))
# print(np.mean(arr, axis=0))
# print(np.median(arr, axis=1))
# print(np.median(arr, axis=0))

#percentile
arr=np.array([10,14,17,25,40,60,45,30,100,90,80,70,40,50])
# print(np.percentile(arr,50))
# print(np.sort(arr))

#quantile
print(np.quantile(arr,0.3))