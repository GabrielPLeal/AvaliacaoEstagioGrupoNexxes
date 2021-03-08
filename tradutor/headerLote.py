from modeloArquivo import dicTradu, listaArquivo

dicHeaderLote = {}

cont = 1

while cont <= len(dicTradu):
    if dicTradu[cont] == 'HL':
        print(dicTradu[cont])
        print(listaArquivo[cont - 1])
        linhaArq = listaArquivo[cont - 1]
        # ---Controle---
        dicHeaderLote['codBanco'] = int(linhaArq[0:3])
        dicHeaderLote['loteServico'] = int(linhaArq[3:7])
        dicHeaderLote['tipoReg'] = int(linhaArq[7])
        # ---Serviço---
        dicHeaderLote['tipoOpe'] = linhaArq[8]
        dicHeaderLote['tipoSer'] = int(linhaArq[9:11])
        dicHeaderLote['formaLanc'] = int(linhaArq[11:13])
        dicHeaderLote['numVerLayLote'] = int(linhaArq[13:16])
        dicHeaderLote['usoNex'] = linhaArq[16]
        # ---EMPRESA---
        dicHeaderLote['tipoInscEmp'] = int(linhaArq[17])
        dicHeaderLote['numInscEmp'] = int(linhaArq[18:32])
        dicHeaderLote['codConvBan'] = linhaArq[32:52]
        dicHeaderLote['agMantCont'] = int(linhaArq[52:57])
        dicHeaderLote['digVerAg'] = linhaArq[57]
        dicHeaderLote['numContCor'] = int(linhaArq[58:70])
        dicHeaderLote['digVerCont'] = linhaArq[70]
        dicHeaderLote['digVerAgCont'] = linhaArq[71]
        dicHeaderLote['nomeEmp'] = linhaArq[72:102]
        dicHeaderLote['mensagem'] = linhaArq[102:142]
        # ---Endereço da Empresa---
        dicHeaderLote['logradouro'] = (linhaArq[142:172])
        dicHeaderLote['numero'] = int(linhaArq[172:177])
        dicHeaderLote['complemento'] = linhaArq[177:192]
        dicHeaderLote['cidade'] = linhaArq[192:212]
        dicHeaderLote['cep'] = int(linhaArq[212:217])
        dicHeaderLote['compCep'] = linhaArq[217:220]
        dicHeaderLote['estado'] = linhaArq[220:222]
        dicHeaderLote['usoExcNex'] = linhaArq[222:230]
        dicHeaderLote['codOcoRet'] = linhaArq[230:240]
        print(dicHeaderLote)
        cont = cont + 1
        break
    else:
        cont = cont + 1
