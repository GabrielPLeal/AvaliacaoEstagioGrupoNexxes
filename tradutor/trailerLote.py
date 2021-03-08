from modeloArquivo import dicTradu, listaArquivo

dicTraLote = {}

cont = 1

while cont <= len(dicTradu):
    if dicTradu[cont] == 'TL':
        print(dicTradu[cont])
        print(listaArquivo[cont - 1])
        linhaArq = listaArquivo[cont - 1]
        # ---Controle---
        dicTraLote['codBanco'] = int(linhaArq[0:3])
        dicTraLote['loteServico'] = int(linhaArq[3:7])
        dicTraLote['tipoReg'] = int(linhaArq[7])
        dicTraLote['usoNex'] = linhaArq[8:17]
        # ---Totais---
        dicTraLote['quantRegLot'] = int(linhaArq[17:23])
        dicTraLote['somaVal'] = int(linhaArq[23:41])
        dicTraLote['somaQtdMoedas'] = int(linhaArq[41:59])
        dicTraLote['numAvisoDeb'] = int(linhaArq[59:65])
        dicTraLote['usoExcNex'] = linhaArq[65:230]
        dicTraLote['codOcRet'] = linhaArq[230:240]
        print(dicTraLote)
        cont = cont + 1
        break
    else:
        cont = cont + 1