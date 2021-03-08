import sys

entrada = sys.argv[1]
saida = sys.argv[2]

arquivo = open(entrada, 'r')
listaArquivo = arquivo.readlines()
classe = ''
dicTradu = {}


for cont in listaArquivo:
    if int(cont[7]) == 0:
        classe = 'HA' # Header de arquivo
        dicTradu[listaArquivo.index(cont) + 1] = classe
    elif int(cont[7]) == 1:
        classe = 'HL' # Header de lote
        dicTradu[listaArquivo.index(cont) + 1] = classe
    elif int(cont[7]) == 3:
        classe = 'RD' # Registro de detalhe
        dicTradu[listaArquivo.index(cont) + 1] = classe
    elif int(cont[7]) == 5:
        classe = 'TL' # Trailer de lote')
        dicTradu[listaArquivo.index(cont) + 1] = classe
    elif int(cont[7]) == 9:
        classe = 'TA' # Trailer de arquivo
        dicTradu[listaArquivo.index(cont) + 1] = classe
    else:   
        print('[ERRO] Classe de modelo de arquivo inexistente.')    
