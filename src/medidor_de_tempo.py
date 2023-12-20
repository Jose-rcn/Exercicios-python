#decorador capaz de calcular o tempo de execução de uma função
from datetime import datetime
from time import sleep
def medidor_de_tempo(func):
    def inner(*args, **kwargs):
        Tempo_inicial = datetime.now()
        resultado = func(*args, **kwargs)
        tempo_final = datetime.now()
        tempo_exec = tempo_final - Tempo_inicial
        print(f'Tempo de execuçãõ da função: {tempo_exec.total_seconds()}')
        return resultado
    return inner

@medidor_de_tempo
def soma(x,y):
    sleep(2)
    return x + y
print(soma(12,2))