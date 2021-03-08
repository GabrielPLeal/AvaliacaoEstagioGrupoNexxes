from modeloArquivo import dicTradu, listaArquivo

dicTraArq = {}

cont = 1

while cont <= len(dicTradu):
    if dicTradu[cont] == 'TA':
        linhaArq = listaArquivo[cont - 1]
        # ---Controle---
        dicTraArq['codBanco'] = int(linhaArq[0:3])
        dicTraArq['loteServico'] = int(linhaArq[3:7])
        dicTraArq['tipoReg'] = int(linhaArq[7])
        dicTraArq['usoNex'] = linhaArq[8:17]
        # ---Totais---
        dicTraArq['qtdLotArq'] = int(linhaArq[17:23])
        dicTraArq['qtdRegArq'] = int(linhaArq[23:29])
        dicTraArq['qtdContConc'] = int(linhaArq[29:35])
        dicTraArq['usoExcNex'] = linhaArq[35:240]
        print(dicTraArq)
        cont = cont + 1
        break
    else:
        cont = cont + 1