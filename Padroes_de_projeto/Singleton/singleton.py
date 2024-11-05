class Singleton:
    def __new__(cls,*args, **kwargs):
        if not hasattr(cls,"instance"):
            cls.instance = super(Singleton,cls).__new__(cls) #cria o objeto
        return cls.instance
    def __init__(self, value:int) -> None:
        self.value = value
    

o1 = Singleton(100)
o2 = Singleton(300)
print(id(o1))
print(id(o2))

