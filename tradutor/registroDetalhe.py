from modeloArquivo import dicTradu, listaArquivo

dicRegDet = {}
dicRegsDets = {}

primCont = 1
segCont = 1

while primCont <= len(dicTradu):
    if dicTradu[primCont] == 'RD':
        linhaArq = listaArquivo[primCont - 1]
        # ---primControle---
        dicRegDet['codBanco'] = int(linhaArq[0:3])
        dicRegDet['loteServico'] = int(linhaArq[3:7])
        dicRegDet['tipoReg'] = int(linhaArq[7])
        # ---Serviço---
        dicRegDet['numReg'] = int(linhaArq[8:13])
        dicRegDet['codSegReg'] = linhaArq[13]
        dicRegDet['tipoMov'] = int(linhaArq[14])
        dicRegDet['codInstMov'] = int(linhaArq[15:17])
        # ---Favorecido/Crédito--
        dicRegDet['codCamCent'] = int(linhaArq[17:20])
        dicRegDet['codBancoFav'] = int(linhaArq[20:23])
        dicRegDet['agMantprimContFav'] = int(linhaArq[23:28])
        dicRegDet['digVerAg'] = (linhaArq[28])
        dicRegDet['numprimContCor'] = int(linhaArq[29:41])
        dicRegDet['digVerprimCont'] = linhaArq[41]
        dicRegDet['digVerAgprimCont'] = linhaArq[42]
        dicRegDet['nomeFav'] = linhaArq[43:73]
        dicRegDet['numDocAtrEmp'] = linhaArq[73:93]
        dicRegDet['dataPag'] = int(linhaArq[93:101])
        dicRegDet['tipoMoeda'] = linhaArq[101:104]
        dicRegDet['quantMoeda'] = int(linhaArq[104:119])
        dicRegDet['valPag'] = int(linhaArq[119:134])
        dicRegDet['numDocAtrBanc'] = linhaArq[134:154]
        dicRegDet['dataReal'] = int(linhaArq[154:162])
        dicRegDet['ValReal'] = int(linhaArq[162:177])
        dicRegDet['info2'] = linhaArq[177:217]
        dicRegDet['codDoc'] = linhaArq[217:219]
        dicRegDet['codFinTed'] = linhaArq[219:224]
        dicRegDet['codLanc'] = linhaArq[224:229]
        dicRegDet['aviso'] = linhaArq[230]
        dicRegDet['ocorrencias'] = linhaArq[230:240]

        dicRegsDets['cliente' + str(segCont)] = dicRegDet
        primCont = primCont + 1
        segCont = segCont + 1
    else:
        primCont = primCont + 1

