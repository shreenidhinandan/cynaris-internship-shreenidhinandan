import numpy as np

# 1D Array
arr1 = np.array([10, 20, 30, 40])
print("1D Array:", arr1)
print("1D Shape:", arr1.shape)

# 2D Array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:\n", arr2)
print("2D Shape:", arr2.shape)

# 3D Array
arr3 = np.array([[[1, 2], [3, 4]],
                 [[5, 6], [7, 8]]])
print("\n3D Array:\n", arr3)
print("3D Shape:", arr3.shape)
# Broadcasting
a = np.array([10, 20, 30])
b = 5

print("\nBroadcasting:", a + b)

# Vectorised Operations
x = np.array([1, 2, 3, 4])
y = np.array([5, 6, 7, 8])

print("Addition:", x + y)
print("Multiplication:", x * y)
print("Subtraction:", x - y)

# Matrix Multiplication
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])

result = np.dot(m1, m2)

print("Matrix Multiplication:\n", result)