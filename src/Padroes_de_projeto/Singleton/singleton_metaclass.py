from typing import Any
class MetaSingleton(type):
    __instances = {}
    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        if cls not in cls.__instances:
            cls.__instances[cls] = super(MetaSingleton,cls).__call__(*args, **kwargs)
        return cls.__instances[cls]

class Logger(metaclass=MetaSingleton):
    ...
    
class Spooler(metaclass=MetaSingleton):
    ...
    
log1 = Logger()
log2 = Logger()
print(id(log1))
print(id(log2))

s1 = Spooler()
s2 = Spooler()
print(id(s1))
print(id(s2))