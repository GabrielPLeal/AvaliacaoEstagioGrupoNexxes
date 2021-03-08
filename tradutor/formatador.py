from modeloArquivo import saida
from headerArquivo import dicHeaderArq
from headerLote import dicHeaderLote
from registroDetalhe import dicRegDet
from trailerArquivo import dicTraArq
from trailerLote import dicTraLote

arquivo = open('../exemplo_relatorio.html', 'r')
exeRel = arquivo.readlines()
#print(exeRel)
arquivo = open(saida, 'w')
print(arquivo)