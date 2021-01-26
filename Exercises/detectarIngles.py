#Módulo detectar inglês

import string

LETRAS_E_ESPAÇOS = string.ascii_letters + string.whitespace

def carregarDicionario():
    arquivoDicionario = open("dictionary.txt")
    palavrasIngles = {}
    for palavra in arquivoDicionario.read().split('\n'):
        palavrasIngles[palavra] = None
    arquivoDicionario.close()
    return palavrasIngles

PALAVRAS_INGLES = carregarDicionario()

def removerNaoLetras(mensagem):
    apenasLetras = []
    for caractere in mensagem:
        if caractere in LETRAS_E_ESPAÇOS:
            apenasLetras.append(caractere)
    return ''.join(apenasLetras)

def calcularRazaoPalavrasIngles(mensagem):
    mensagem = mensagem.upper()
    mensagem = removerNaoLetras(mensagem)
    palavrasPossiveis = mensagem.split()

    if palavrasPossiveis == []:
        return 0.0

    compativeis = 0
    for palavra in palavrasPossiveis:
        if palavra in PALAVRAS_INGLES:
            compativeis += 1
    return compativeis / len(palavrasPossiveis)

def calcularRazaoLetrasIngles(mensagem):
    numeroLetras = len(removerNaoLetras(mensagem))
    return numeroLetras / len(mensagem)

def podeSerIngles(mensagem, palavrasPorcentagem = 50, letrasPorcentagem = 85):
    palavrasCompativeis = calcularRazaoPalavrasIngles(mensagem) * 100 >= palavrasPorcentagem
    letrasCompativeis = calcularRazaoLetrasIngles(mensagem) * 100 >= letrasPorcentagem
    return palavrasCompativeis and letrasCompativeis
