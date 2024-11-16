from abc import ABC, abstractmethod

# Assunto/ tópico
class Agencia_de_noticias:
    def __init__(self) -> None:
        self._inscritos =[]
        self._ultima_noticia = None
        
    def inscrever(self, inscrito):
        self._inscritos.append(inscrito)
        
    def desinscrever(self, inscrito= None):
        if not inscrito:
            return self._inscritos.pop()
        self._inscritos.remove(inscrito)
        
    def notificar_todos(self):
        for i in self._inscritos:
            i.notificar()
    
    def mostrar_noticia(self):
        return self._ultima_noticia
    def adicionar_noticia(self, noticia):
        self._ultima_noticia = noticia
        self.notificar_todos()
        
    def get_inscritos(self):
        return self._inscritos
    
# Interface Observador
class Observer(ABC):
    @abstractmethod
    def notificar(self):
        pass

#Observadores Concretos
class ObservadoresEmail(Observer):
    def __init__(self, agencia:Agencia_de_noticias) -> None:
        self._pessoas = []
        self.agencia_noticia = agencia
        self.agencia_noticia.inscrever(self)
    def notificar(self):
        for pessoa in self._pessoas:
            print(f'E-mail enviado para {pessoa}: {self.agencia_noticia.mostrar_noticia()}')
    def adicionar_pessoa(self,pessoa):
        self._pessoas.append(pessoa)
#Observadores Concretos       
class ObservadoresSMS(Observer):
    def __init__(self, agencia:Agencia_de_noticias) -> None:
        self._pessoas = []
        self.agencia_noticia = agencia
        self.agencia_noticia.inscrever(self)
    def notificar(self):
        for pessoa in self._pessoas:
            print(f'SMS enviado para {pessoa}: {self.agencia_noticia.mostrar_noticia()}')
    def adicionar_pessoa(self,pessoa):
        self._pessoas.append(pessoa)
        
class Pessoa:
    def __init__(self, name) -> None:
        self.name = name
    def __repr__(self) -> str:
        return self.name
        
if __name__ == '__main__':
    agencia = Agencia_de_noticias()
    email = ObservadoresEmail(agencia)
    sms = ObservadoresSMS(agencia)
    
    joao = Pessoa('João')
    maria = Pessoa('Maria')
    
    email.adicionar_pessoa(joao)
    sms.adicionar_pessoa(joao)
    sms.adicionar_pessoa(maria)
    
    agencia.adicionar_noticia('Donald Trump é eleito presidente dos estados unidos')