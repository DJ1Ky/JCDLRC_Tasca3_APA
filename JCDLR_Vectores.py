"""

    Nombre: Juan Camilo De Los Ríos
    Práctica 3: Clase usada para trabajar con vectores
    
"""


class Vector:

    
     def __init__(self, iterable = []):
        self.vector = [valor for valor in iterable]



        def __repr__(self):
            return 'Vector(' + repr(self.vector) + ')'



        def __eq__(self, other):
            return self.vector == other.vector

    
    # Per saber la longitud dels vectors 

        def __len__(self):
            return len(self.vector)

    # Accès als elements del vector

        def __getitem__(self,key):
            return self.vector[key]

    # Sobrecárrega de operadors básics

        def __add__(self, other):
            if isinstance(other, (int, float, complex)):     
                return Vector(item + other for item in self)
            else:
                return Vector([item + otro for item, otro in zip(self, other)])


        def __neg__(self):
            return Vector([-item for item in self])


        def __sub__(self,other):
            if isinstance (other, (int, float, complex)):
                return Vector(item - other for item in self)
            else:
                return Vector([item - otro for item, otro in zip(self, other)])


        __radd__ = __add__


        __iadd__ = __add__ 


    
    # Sobrecarreguem l'operador (*) per implementar la multiplicació d'un vector per una constant o altre vector
        
        def __mul__(self, other):
            if isinstance(other, (int,float,complex)):
                return Vector([item * other for item in self])
            else:
                return Vector([item * otro for item, otro in zip(self,other)])


        __rmul__ = __mul__


    # Sobrecarreguem l'operador @ per implementar el productw escalar de dos vectors
    
        def __matmul__(self, other):
            ini = 0
            mul = Vector([item * otro for item, otro in zip(self, other)])
            for i in range(len(mul)):
                ini += mul[i]
            return ini


        __rmatmul__ = __matmul__


    # Sobrecarreguem l'operador // per que proporcioni la component tangencial

        def __floordiv__(self, other):
            suma = 0
            for x in range(len(other)):
                suma += other[x]**2
            vtan = ((self @ other)/suma)*other
            return vtan

    
        __rfloordiv__ = __floordiv__

    
    # Sobrecarreguem l'operador % per que proporcioni la component normal

        def __mod__(self,other):          
            vtan = self // other
            vper = self - vtan
            return vper


        __rmod__= __mod__


v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])






