from db import _executar
from typing import Optional, Type
class Produto:
    def __init__(self, nome, preco, id=None) -> None:
        self.id = id
        self.nome = nome
        self.preco = preco
        self.status = 1
        
        query = '''
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    preco REAL,
    status NUMERIC
)
'''
        _executar(query)
    def salvar_produto(self):
        query = f'INSERT INTO produtos (nome, preco, status) VALUES {(self.nome,float(self.preco),self.status)}'
        _executar(query)
    
    def atualizar_status(self):
        query = f'UPDATE produtos SET status={self.status} WHERE id={self.id}'
        _executar(query)
    def deletar(self):
        query = f'DELETE FROM produtos WHERE id={self.id}'
        _executar(query)
    
    @staticmethod
    def get_produtos():
        query = 'SELECT * FROM produtos'
        produtos = _executar(query)
        return produtos

    @staticmethod
    def get_produto(id):
        query = f'SELECT id, nome, preco FROM produtos WHERE id={int(id)}'
        produto = _executar(query)[0] # type: ignore
        produto = Produto(id=produto[0],nome=produto[1],preco=produto[2]) # type: ignore
        return produto