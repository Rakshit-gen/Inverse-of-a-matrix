import numpy as np
a=float(input('enter coefficient x1'))
b=float(input('enter coefficient x2'))
c=float(input('enter coefficient x3'))
d=float(input('enter coefficient y1'))
e=float(input('enter coefficient y2'))
f=float(input('enter coefficient y3'))
de=float(input('enter coefficient z1'))
ce=float(input('enter coefficient z2'))
fe=float(input('enter coefficient z3'))
g=float(input('enter coefficient c1'))
h=float(input('enter coefficient c2'))
i=float(input('enter coefficient c3'))
se=np.array(([a,b,c],
             [d,e,f],
             [de,ce,fe]))
pi=np.array(([g,h,i]))
sol=np.linalg.inv(se).dot(pi)
print(sol)
