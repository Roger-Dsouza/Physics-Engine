from numpy import *
from numpy import *
[]
{}
def restitute(m1,m2,u1,u2,e): #Assumes two particles are approaching before colliding and seperating afterwards.
    m1=float(m1)
    m2=float(m2)
    u1=float(u1)
    u2=float(u2)*-1
    e=float(e)

    if m1==m2:
       v1=((e-1)/2)*u1+((e+1)/2)*u2
       v2=((e+1)/2)*u1+((e-1)/2)*u2
       l=[v1,v2] 
       
    else:
       operator=array([[-m1,m2],[1,1]])
       qvector=array([[(m1*u1)-(m2*u2)],[e*(u1+u2)]])
       inverse=linalg.inv(operator)
       avector=dot(inverse,qvector)
       v1=-1*avector[0][0]
       v2=avector[1][0]
       l=[v1,v2]     
       

    

    
    
    return l 
  


