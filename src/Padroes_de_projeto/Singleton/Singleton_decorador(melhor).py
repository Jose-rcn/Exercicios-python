def singleton(the_class,*args, **kwargs):
    instances = {}
    def get_class(*args, **kwargs):
        if the_class not in instances:
            instances[the_class] = the_class(*args, **kwargs)
        return instances[the_class]
    return get_class
    
@singleton
class AppSettings:
    def __init__(self) -> None:
        print('init executado apenas uma vez')
        self.tema = 'Tema Escuro'
        self.font = '18px'
        
if __name__ == '__main__':
    app1 = AppSettings()
    app1.tema = 'Claro'
    app2 = AppSettings()
    print(app2.tema)
    