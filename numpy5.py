#Handle missing data using NUMPY

import numpy as np;
# arr=np.array([10,np.nan,20,np.nan,40,50])  #nan=not a number
# print(arr.size)
# print(arr.ndim)
# print(arr)
# print(np.isnan(arr)) #to check if the data is missing or not
# print(np.isnan(arr).sum())

# clean_data=arr[~np.isnan(arr)] #deleting missing data
# print(clean_data.astype(int))

# print(arr)
# arr[np.isnan(arr)]=0
# print(arr)

# mean=np.nanmean(arr)
# arr[np.isnan(arr)]=mean #replacing by mean
# print(arr)

# median=np.nanmedian(arr)
# arr[np.isnan(arr)]=median
# print(arr)

# print(arr)
# print(np.nansum(arr))
# print(np.nanmax(arr))
# print(np.nanmin(arr))

# arr=np.array([[1,2,np.nan],[4,np.nan,6]])
# print(np.nansum(arr))
# print(np.nansum(arr,axis=1))
# print(np.nansum(arr,axis=0))

# arr=np.array([10,20,np.nan,30,np.nan])
# arr_filled=np.nan_to_num(arr,nan=1) #replacing nan with given number
# print(arr_filled)

# print(np.prod(arr_filled))

# sales=np.array([1000,2000,1500,3000])
# growth_factor=np.array([1.1,np.nan,0.95,np.nan])
# growth_factor=np.nan_to_num(growth_factor,nan=1)
# final=sales*growth_factor
# print(final)

# data=[10,12,13,14,15,100] #right skewed
# ages=np.array([20,25,np.nan,30,35],dtype=float)
# mean_age=np.nanmean(ages)
# print(mean_age)

# data=[10,85.88,90,92,95] #left skewed

# income=[30000,35000,40000,500000,np.nan]
# income=np.array(income,dtype=float)
# print("Original Income: ",income)
# median_income=np.nanmedian(income)
# income[np.isnan(income)]=median_income
# print(income)

# arr=np.array([5,np.nan,15])
# arr=np.nan_to_num(arr,nan=-1)
# print(arr)
