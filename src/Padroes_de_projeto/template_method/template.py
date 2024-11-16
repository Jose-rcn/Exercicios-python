from abc import ABC,abstractmethod

class Compilador(ABC):
    @abstractmethod
    def coletar_fonte(self):
        ...
    @abstractmethod
    def compilar_objeto(self):
        ...
    @abstractmethod
    def executar(self):
        ...
    def compilar_e_executar(self):
        self.coletar_fonte()
        self.compilar_objeto()
        self.executar()
        
class CompiladorIOS(Compilador):
    def coletar_fonte(self):
        print('Código fonte swift coletado')
    def compilar_objeto(self):
        print('Código Swift compilado')
    def executar(self):
        print('Programa IOS em execução')

class CompiladorAndroid(Compilador):
    def coletar_fonte(self):
        print('Código fonte kotlin coletado')
    def compilar_objeto(self):
        print('Código kotlin compilado')
    def executar(self):
        print('Programa android em execução')

if __name__ == '__main__':
    compilador_ios = CompiladorIOS()
    compilador_ios.compilar_e_executar()
    
    compilador_android = CompiladorAndroid()
    compilador_android.compilar_e_executar()