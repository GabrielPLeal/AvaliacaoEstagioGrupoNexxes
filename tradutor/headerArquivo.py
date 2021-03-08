from modeloArquivo import dicTradu, listaArquivo

dicHeaderArq = {}

cont = 1

while cont <= len(dicTradu):
    if dicTradu[cont] == 'HA':
        linhaArq = listaArquivo[cont - 1]
        # ---Controle---
        dicHeaderArq['codBanco'] = int(linhaArq[0:3])
        dicHeaderArq['loteServico'] = int(linhaArq[3:7])
        dicHeaderArq['tipoReg'] = int(linhaArq[7])
        dicHeaderArq['usoNex'] = linhaArq[8:17]
        # ---EMPRESA---
        dicHeaderArq['tipoInscEmp'] = int(linhaArq[17])
        dicHeaderArq['numInscEmp'] = int(linhaArq[18:32])
        dicHeaderArq['codConvBan'] = linhaArq[32:52]
        dicHeaderArq['agMantCont'] = int(linhaArq[52:57])
        dicHeaderArq['digVerAg'] = linhaArq[57]
        dicHeaderArq['numContCor'] = int(linhaArq[58:70])
        dicHeaderArq['digVerCont'] = linhaArq[70]
        dicHeaderArq['digVerAgCont'] = linhaArq[71]
        dicHeaderArq['nomeEmp'] = linhaArq[72:102]
        dicHeaderArq['nomeBanco'] = linhaArq[102:132]
        dicHeaderArq['nomeVan'] = linhaArq[132:142]
        # ---Arquivo---
        dicHeaderArq['codRemRet'] = int(linhaArq[142])
        dicHeaderArq['dataGerArq'] = int(linhaArq[143:151])
        dicHeaderArq['horaGerArq'] = int(linhaArq[151:157])
        dicHeaderArq['numSeqArq'] = int(linhaArq[157:164])
        dicHeaderArq['numVerLayArq'] = int(linhaArq[164:167])
        dicHeaderArq['denGravArq'] = int(linhaArq[167:172])
        dicHeaderArq['usoResBanco'] = linhaArq[172:191]
        dicHeaderArq['usoResEmp'] = linhaArq[191:211]
        dicHeaderArq['usoExcNex'] = linhaArq[211:240]
        print(dicHeaderArq)
        cont = cont + 1
    else:
        cont = cont + 1

    

