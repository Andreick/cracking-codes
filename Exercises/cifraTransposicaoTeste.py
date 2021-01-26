#Teste da Cifra de Transposição

import time, string, random, sys, cifraTransposicaoCriptografia, cifraTransposicaoDescriptografia

def main():
    random.seed(94)
    #atribui um valor estático à "random seed" para gerar sempre a mesma sequência de números aleatórios.

    tempoInicial = time.time() #inicia a contagem dos segundos.

    for i in range(20):
        #Gera 20 mensagens aleatórias para testar.

        mensagem = string.printable[:94] * random.randint(4,38)
        #a mensagem terá um tamanho aleatório.

        mensagem = list(mensagem)
        random.shuffle(mensagem)
        mensagem = ''.join(mensagem[:300 * random.randint(4, 12)]) #evita que a mensagem tenha caracteres com quantidade na mesma proporção.
        #converte a mensagem em lista, embaralha os caracteres e converte de volta em string.

        print('Teste #%d: "%s..."\nTestando...\n' %(i+1, mensagem[:60]))
        

        for chave in range(1, int(len(mensagem)/2)):
            #checa todas as chaves possíveis para cada mensagem.
            
            criptografado = cifraTransposicaoCriptografia.criptografarMensagem(mensagem, chave)
            descriptografado = cifraTransposicaoDescriptografia.descriptografarMensagem(criptografado, chave)

            if mensagem != descriptografado:
                #se a descriptografia não bate com a mensagem original, exibe uma mensagem de erro e encerra o programa.

                print('Incompatibilidade com a chave %d e a mensagem %s' %(chave, mensagem))
                print('Descriptografado como:', descriptografado)
                sys.exit()

    tempoTotal = round(time.time() - tempoInicial, 2) #calcula quanto tempo os testes levaram.

    print("Tempo de verificação:", tempoTotal, "segundos")
    print("Teste da cifra de transposição aprovado")

if __name__ == '__main__':
    main()
