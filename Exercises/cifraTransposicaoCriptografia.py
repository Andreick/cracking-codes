#Criptografia usando crifra de transposição

import pyperclip

def main():
    mensagem_escolhida = "Whoever said practice makes perfect was an idiot. Humans can't be perfect because we're not machines. The best thing you can say about practice is that it makes...better. Those are three of my least favorite things. Oh, and eating raisins because I don't like to eat things with wrinkles. Autism isn't an accomplishment. It's something I was born with. You wouldn't write an essay about having ten fingers and ten toes, would you? No, because that would be really, really, really, really dumb. So I'll stick with the boobs." #mensagem a ser criptografada.
    chave_escolhida = 111 #chave utilizada na criptografia.
    
    mensagem_criptografada = criptografarMensagem(mensagem_escolhida, chave_escolhida)
    #chama a função que faz a criptografia e armazena a mensagem criptografada em uma variável.

    print("Mensagem criptografada:", mensagem_criptografada + '|') #exibe a mensagem criptografada.
    #o '|' serve para marcar o fim da mensagem que pode conter espaços em branco no final.

    pyperclip.copy(mensagem_criptografada) #envia a mensagem criptografada para a área de transferência do computador.

def criptografarMensagem(mensagem, chave):
    texto_cifrado = [''] * chave #cada string da lista representa uma coluna.

    coluna = 0 #esta variável será utilizada como índice da lista.

    for caractere in mensagem:
        #itera sobre cada caractere da mensagem.
        
        texto_cifrado[coluna] += caractere #cada caractere é inserido em sua respectiva coluna.

        coluna +=1 #pula para a próxima coluna.
        if coluna == chave:
            #quando todas as colunas estiverem preenchidas, a coluna volta ao início, simulando a troca de linha.
            coluna = 0
    #aqui, todos os caracteres da mensagem estão armazenados em uma lista e embaralhados conforme a cifra de transposição.

    return ''.join(texto_cifrado) #a função junta as strings da lista e retorna uma única string que é a mensagem criptografada.

if __name__ == '__main__':
    main()
