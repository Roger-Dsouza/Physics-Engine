class Vector:
    def __init__(self,vector:list[int,float]):
        self.vector=vector

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


a=Vector([1,2,1])
b=Vector([2,3,4])
print(a.dot(b))                
