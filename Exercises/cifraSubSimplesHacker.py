#Programa Hacker - Cifra de Substituição Simples

import os, copy, string, pyperclip, cifraSubSimples, wordPatterns, makeWordPatterns

LETRAS = string.ascii_uppercase
NAO_LETRAS = string.digits + string.punctuation + string.whitespace[1:]

def gerarMapaBranco():
    mapa = {}
    for char in LETRAS:
        mapa[char] = []
    return mapa

def main():
    mensagem = '''OLQIHXIRCKGNZ PLQRZKBZB
MPBKSSIPLC'''
    
    #Determina a possível tradução de cada letra:
    print("Hackeando...")
    mapeamentoLetras = hackearSubSimples(mensagem)
    mensagemHackeada = descriptografarComMapeamentoDeLetrasCifradas(mensagem, mapeamentoLetras)

    #Exibe os resultados ao usuário:
    print("Mapeamento:")
    print(mapeamentoLetras)
    print("\nMensagem cifrada:")
    print(mensagem)
    print("\nMensagem hackeada:")
    print(mensagemHackeada)

def adicionarLetrasAoMapeamento(mapeamentoLetras, palavraCifrada, candidato):
    for i in range(len(palavraCifrada)):
        if candidato[i] not in mapeamentoLetras[palavraCifrada[i]]:
            mapeamentoLetras[palavraCifrada[i]].append(candidato[i])

def cruzarMapas(mapaA, mapaB):
    mapaCruzado = gerarMapaBranco()
    for letra in LETRAS:
        if mapaA[letra] == []:
            mapaCruzado[letra] = copy.deepcopy(mapaB[letra])
        elif mapaB[letra] == []:
            mapaCruzado[letra] = copy.deepcopy(mapaA[letra])
        else:
            for letraMapeada in mapaA[letra]:
                if letraMapeada in mapaB[letra]:
                    mapaCruzado[letra].append(letraMapeada)

    return mapaCruzado

def removerLetrasResolvidasDoMapeamento(mapeamentoLetras):
    loopNovamente = True
    while loopNovamente:
        loopNovamente = False
        letrasResolvidas = []
        for letraCifrada in LETRAS:
            if len(mapeamentoLetras[letraCifrada]) == 1:
                letrasResolvidas.append(mapeamentoLetras[letraCifrada][0])
        for letraCifrada in LETRAS:
            for letra in letrasResolvidas:
                if len(mapeamentoLetras[letraCifrada]) != 1 and letra in mapeamentoLetras[letraCifrada]:
                    mapeamentoLetras[letraCifrada].remove(letra)
                    if len(mapeamentoLetras[letraCifrada]) == 1:
                        #Uma nova letra está resolvida agora, então o loop se repete.
                        loopNovamente = True

def gerarLPC(mensagem):
    mensagem = mensagem.upper()
    for char in NAO_LETRAS:
            mensagem = mensagem.split(char)
            mensagem = ''.join(mensagem)
    return mensagem.split()

def hackearSubSimples(mensagem):
    mapaCruzado = gerarMapaBranco()
    listaPalavrasCifradas = gerarLPC(mensagem)
    for palavraCifrada in listaPalavrasCifradas:
        mapaCandidatos = gerarMapaBranco()
        padraoPalavra = makeWordPatterns.getWordPattern(palavraCifrada)
        if padraoPalavra not in wordPatterns.allPatterns:
            continue #se esta palavra não está no dicionário, continue.
        for candidato in wordPatterns.allPatterns[padraoPalavra]:
            adicionarLetrasAoMapeamento(mapaCandidatos, palavraCifrada, candidato)
        mapaCruzado = cruzarMapas(mapaCruzado, mapaCandidatos)
    removerLetrasResolvidasDoMapeamento(mapaCruzado)

    return mapaCruzado

def descriptografarComMapeamentoDeLetrasCifradas(textoCifrado, mapeamentoLetras):
    chave = ['_'] * len(LETRAS)
    for letraCifrada, letras in mapeamentoLetras.items():
        if len(letras) == 1:
            indiceChave = LETRAS.find(letras[0])
            chave[indiceChave] = letraCifrada
        else:
            textoCifrado = textoCifrado.replace(letraCifrada.lower(), '_')
            textoCifrado = textoCifrado.replace(letraCifrada.upper(), '_')
    chave = ''.join(chave)

    return cifraSubSimples.descriptografarMensagem(textoCifrado, chave)

if __name__ == '__main__':
    main()
