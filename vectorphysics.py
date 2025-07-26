from math import *
class Vector:
    def __init__(self,vector:list[int,float]):
        self.vector=vector

    def magnitude(self):
        total=0
        for a in self.vector:
            total+=a**2
        return sqrt(total)        

    def __add__(self,other):
        ret=[]
        if isinstance(other,Vector):
            if len(other.vector)!=len(self.vector):
                raise TypeError("Vectors have to be in the same vector space.")
            else:
                for a in range(0,len(other.vector),1):
                    ret.append(self.vector[a]+other.vector[a])
                return Vector(ret).vector
        else:
            raise TypeError("Unsupported operation between vector and non-vector.")
    __radd__=__add__

    def __sub__(self,other):
        ret=[]
        if isinstance(other,Vector):
            if len(other.vector)!=len(self.vector):
                raise TypeError("Vectors have to be in the same vector space.")
            else:
                for a in range(0,len(other.vector),1):
                    ret.append(self.vector[a]-other.vector[a])
                return Vector(ret).vector
        else:
            raise TypeError("Unsupported operation between vector and non-vector.")
    __rsub__=__sub__

    def dot(self,other):
        total=0
        if isinstance(self,Vector) and isinstance(other,Vector):
            if len(self.vector)==len(other.vector):
                for a in range(0,len(other.vector),1):
                    total+=other.vector[a]*self.vector[a]
                return total

    def angleBetween(self,other):
        options=[]
        if isinstance(self,Vector) and isinstance(other,Vector):
            if len(self.vector)==len(other.vector):
                options.append(acos(a.dot(b)/(a.magnitude()*b.magnitude())))
                options.append(pi-acos(a.dot(b)/(a.magnitude()*b.magnitude())))

        return options        
               



a=Vector([1,2,1])
b=Vector([2,3,4])
print(((a.angleBetween(b)[0])/(2*pi)*360))             
