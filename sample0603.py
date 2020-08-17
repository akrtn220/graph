import numpy as np

# mat0=np.matrix([1,0])
mat1=np.matrix([[0.7,0.3],[0.8,0.2]])
# mat1=np.matrix([1,0])*mat
# print(mat1)
# mat2=mat1*mat
# print(mat2)
# for i in range(0,9):
#     _mat=mat0*mat
#     print(_mat)
#     mat0=_mat

# mat0=np.matrix([0.3,0.2,0.5])
# mat2=np.matrix([
#     [0.3,0.2,0.5],
#     [0.8,0.1,0.1],
#     [0.7,0.2,0.1]]
#     )
# for i in range(0,9):
#     _mat=mat0*mat2
#     print(_mat)
#     mat0=_mat

# A = np.matrix([
# [7,-8,-7],
# [2,-9,2],
# [5,1,-9]
# ])
# Y = np.matrix([
# [0],
# [0],
# [0]
# ])
# np.linalg.inv(A)*Y
# print('{:.3g}'.format(np.linalg.inv(A)*Y))

mat=np.matrix([
    [0.3,0.2,0.5],
    [0.3,0.1,0.6],
    [0.9,0.1,0]]
    )
mat_n=np.matrix([
    [0.3,0.2,0.5],
    [0.3,0.1,0.6],
    [0.9,0.1,0]]
    )

for i in range(0,98):
    mat_n*=mat
print(mat_n)