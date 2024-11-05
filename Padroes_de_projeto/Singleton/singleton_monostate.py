class Monostate:
    __estado = {}
    def __new__(cls,*args, **kwargs):
        obj = super(Monostate,cls).__new__(cls,*args, **kwargs)
        obj.__dict__ =  cls.__estado
        return obj
    
m1 = Monostate()
print(id(m1))
m2 = Monostate()
print(id(m2))

print(m1.__dict__)
print(m2.__dict__)

m1.nome = "AA" # type: ignore

print(m1.__dict__)
print(m2.__dict__)

