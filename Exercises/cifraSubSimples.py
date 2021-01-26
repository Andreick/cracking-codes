#Cifra de substituição simples

import string, pyperclip, sys, random

CONJUNTO_CARACTERES = string.ascii_uppercase #caracteres que poderão ser cifrados.
#caso a mensagem contenha um caractere que não pertence a este conjunto, o caractere não é alterado.

def main():
    mensagemEscolhida = '''If a man is offered a fact which goes against his
instincts, he will scrutinize it closely, and unless the evidence
is overwhelming, he will refuse to believe it. If, on the other
hand, he is offered something which affords a reason for acting
in accordance to his instincts, he will accept it even on the
slightest evidence. The origin of myths is explained in this way.
-Bertrand Russell'''
    chaveEscolhida = gerarChaveAleatoria()
    modoEscolhido = 'criptografar' #Mude para 'criptografar' ou 'descriptografar'.

    if not chaveValida(chaveEscolhida):
        #teste para avaliar se a chave pode ser usada.
        sys.exit('Há um erro na chave ou no conjunto de caracteres.')
    if modoEscolhido == 'criptografar':
        traducao = criptografarMensagem(mensagemEscolhida, chaveEscolhida)
    elif modoEscolhido == 'descriptografar':
        traducao = descriptografarMensagem(mensagemEscolhida, chaveEscolhida)
        
    print('Chave', chaveEscolhida)
    print('mensagem %sda:' %(modoEscolhido[:-1]))
    print(traducao)
    pyperclip.copy(traducao)
    print('\nCopiado para a área de transferência.')

def chaveValida(chave):
    #a chave precisa ter exatamente os mesmos caracteres do conjunto.
    listaChave = list(chave)
    listaConjunto = list(CONJUNTO_CARACTERES)
    listaChave.sort()
    listaConjunto.sort()

    return listaChave == listaConjunto

def criptografarMensagem(mensagem, chave):
    return traduzirMensagem(mensagem, chave, 'criptografar')

def descriptografarMensagem(mensagem, chave):
    return traduzirMensagem(mensagem, chave, 'descriptografar')

def traduzirMensagem(mensagem, chave, modo):
    traducao = ''
    
    charsConjunto = CONJUNTO_CARACTERES
    charsChave = chave
    if modo == 'descriptografar':
        charsConjunto, charsChave = charsChave, charsConjunto

    for caractere in mensagem:
        if caractere.upper() in charsConjunto:
            caractereIndice = charsConjunto.find(caractere.upper())
            if caractere.isupper():
                traducao += charsChave[caractereIndice].upper()
            else:
                traducao += charsChave[caractereIndice].lower()
        else:
            traducao += caractere

    return traducao

def gerarChaveAleatoria():
    #a partir do conjunto de caracteres se obtem uma chave válida.
    chave = list(CONJUNTO_CARACTERES)
    random.shuffle(chave)
    return ''.join(chave)

if __name__ == '__main__':
    main()
