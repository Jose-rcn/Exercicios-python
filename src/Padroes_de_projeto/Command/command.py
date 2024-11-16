from abc import ABC, abstractmethod

#command
class Ordem(ABC):
    @abstractmethod
    def executar(self):
        ...

#comando concreto
class OrdemCompra(Ordem):
    def __init__(self, acao) -> None:
        self.acao = acao
    def executar(self):
        self.acao.comprar()

class OrdemVenda(Ordem):
    def __init__(self, acao) -> None:
        self.acao = acao
    def executar(self):
        self.acao.vender()
        
class Acao:
    def comprar(self):
        print('Você está registrando uma ordem de compra de ações')
        
    def vender(self):
        print('Você está registrando uma ordem de venda de ações')

class Agente:
    def __init__(self) -> None:
        self._fila_ordens = []
    def adicionar_ordem_a_fila(self, ordem):
        self._fila_ordens.append(ordem)
        ordem.executar()
        
if __name__ == '__main__':
    itau = Acao()
    compra = OrdemCompra(itau)
    
    agente = Agente()
    agente.adicionar_ordem_a_fila(compra)