import numpy as np

a = np.array([1,2,3])
print(a)
print(a.T)
b = a.T

print(a.reshape(-1,1))
print(a.reshape(3,1))

aa = np.array([4,5,6])
c = aa.T
print(a+aa)
print(3*a)
print(aa*a)
print(aa/a)

print(np.dot(aa,a))
print(np.dot(b,a))
print(np.dot(c,a))