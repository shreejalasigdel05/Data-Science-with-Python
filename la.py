#linear algebra
import numpy as np;
# #scalar
# a=5
# b=-4

# #vector
# v=np.array([2,4,6])
# print(v)

# #matrix
# mat=np.array([[1,2],[3,4]])
# print(mat)

#dot product (1D)
# a=np.array([1,2,3])
# b=np.array([4,5,6])
# dt=(1*4)+(2*5)+(3*6)
# print(dt)
# print(np.dot(a,b))

#2D
# a=np.array([[1,2],[3,4]])
# b=np.array([[5,6],[7,8]])
# print(np.dot(a,b))
# print(a@b) #dot product shortcut
# rr=(1*5)+(2*7)
# rc=(1*6)+(2*8)
# r11=(3*5)+(4*7)
# r12=(3*6)+(4*8)

#matrix multiplication
# a=np.array([[1,2],[3,4]])
# b=np.array([[5,6],[7,8]])
# print(np.matmul(a,b))

#transpose
# a=np.array([[1,2,3],[4,5,6]])
# print(a)
# print(a.T)

#linear algebra
# a=np.array([[1,2],[3,4]])
# print(np.linalg.inv(a))

# a=np.array([3,4])
# distance=np.linalg.norm(a)
# print(distance)

# a=np.array([2,3])
# b=np.array([5,7])
# dist=a-b 
# euclidean distance
# distance=np.linalg.norm(dist)
# print("Euclidean distance: ",distance)

a=np.array([1,2,3])
b=np.array([-4,-5,-6])
c=np.array([6,6,6])
cosine_similarity_AB=np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))
print(cosine_similarity_AB)
cosine_similarity_AC=np.dot(a,c)/(np.linalg.norm(a)*np.linalg.norm(c))
print(cosine_similarity_AC)