from typing import Union

from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioriaria
from constantes import TIPO_FILA_NORMAL, TIPO_FILA_PRIORITARIA


class FabricaFila:
    @staticmethod
    def pega_fila(tipo_fila: str) -> Union[FilaNormal, FilaPrioriaria]:
        if tipo_fila == TIPO_FILA_NORMAL:
            return FilaNormal()
        elif tipo_fila == TIPO_FILA_PRIORITARIA:
            return FilaPrioriaria()
        else:
            raise NotImplementedError('Tipo de fila não existe')
