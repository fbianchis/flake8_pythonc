import abc
from typing import List

from constantes import TAMANHO_PADRAO_MAXIMO, TAMANHO_PADRAO_MINIM0


class FilaBase(metaclass=abc.ABCMeta): 
    codigo: int = 0  
    fila: List[str] = []
    clientes_atendidos: List[str] = []
    senha_atual: str = ""  

    def reseta_fila(self) -> None:  
        if self.codigo >= TAMANHO_PADRAO_MAXIMO:  
            self.codigo = TAMANHO_PADRAO_MINIM0
        else:
            self.codigo = self.codigo + 1

    def insere_cliente(self):
        self.fila.append(self.senha_atual)

    @abc.abstractclassmethod
    def gera_senha_atual(self):
        ...

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.insere_cliente()

    @abc.abstractclassmethod
    def chama_cliente(self, caixa: int):
        ...
