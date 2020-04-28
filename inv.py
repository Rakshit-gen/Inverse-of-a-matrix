import numpy as np
a=3
b=3
print('enter entries row wise[seperated by space]')
ent=list(map(int,input().split()))
matrix=np.array(ent).reshape(a,b)
print('your matrix is',matrix)
det=np.linalg.det(matrix)
print('determinant of your matrix is',int(det))
if det==0:
    print('no inverse exist')
else:
    inv = np.linalg.inv(matrix)
    print(inv)
    print('adjoint of your matrix', det * inv)
