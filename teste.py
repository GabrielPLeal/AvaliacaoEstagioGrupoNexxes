import sys

entrada = sys.argv[1]
saida = sys.argv[2]

if entrada.endswith('.txt') == False: # Confirmando extensão do arquivo
    print('[ERRO] Arquivo de entrada incorreto')
elif saida.endswith('.txt') == False: # Confirmando extensão do arquivo
    print('[ERRO] Arquivo de saida incorreto')
else:  
    arquivo = open(entrada,'r')
    print(arquivo.readlines()[1])
    print((arquivo.readlines()))

    print(type(entrada))
    print(type(saida))

