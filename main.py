from fila_normal import filanormal
from fila_prioritaria import FilaPrioriaria

# fila_teste = filanormal()
# fila_teste.atualizafila()
# fila_teste.atualizafila()
# fila_teste.atualizafila()
# print(fila_teste.chamacliente(5))
# print(fila_teste.chamacliente(10))

fila_teste_2 = FilaPrioriaria()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
print(fila_teste_2.chamacliente(10))
print(fila_teste_2.chamacliente(1))
print(fila_teste_2.estatistica('10/01/1993', 197, 'detail'))
