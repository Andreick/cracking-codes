#Descriptografia da cifra de transposição

import pyperclip, math

def main():
    mensagem_criptografada = 'QRECBVKTXTYATMLONNWRICZHIMADNHSMUQIHBJAJTQMMVYZAISOXEWMDUHOUWVXHCPOALLYGFPICXDNGASBPGFSFZOGJABCPSZGUNGPGQBERPQCEOEJKNBZZGYQSFXJENHLXFIIURHMTQYYUAGGKZMJKAVTRFEPPHKSIGGPIVITQDCJWMFRHUCLRFLYOGPPKHZVRAQJKCFQNBVYHHDSNAXDKJMERJTBWHBHLWUJEFSAEQPLGRUPTXTWVNIUMEJUVQJMXJTYJCNHFEUVHADNLDBIQCUSIYKZREFYXPLZKEKKRGQOYCSIWOOSWRRVSVKVIOIEIVDXSZKZKODJZDHZXKTVZSFJFHNKHEKZDSTHAQPIVSOIXFCYYCJPBDFLBPJEMUPGGXDKNBKQQFOCOUBHRXIVOGAVFBQTVOHJVXMCWSUOPKCJLXZOHBQCOCHNAAUACWOGSADQCOSOZLGFXKTNTATZXRHFHJJULKXBHDEWWMQRZAXLRZLCZLERQFFELPLILQGCDNYGXHODGHXYOLMSGWYYXWKSSLERVYPMXWBERWTKXLFYGCOHKGHBXMYFXSUVSAWUEZEVJINNUIBEHTFHQDTCBKJYLGWOZWWEKUMVYAENNWMEFRYDMJWMVBGOZIDXFOUIWFCTZFCJZOKTBDZPYEJSRYZTXRLUDUJRNPXZVNCKIDAPARKVVKLZWYPLABNVQQZYVXRNKBHTCAYVABQJTBXYYYLSRJSLIQRFTPDDALGAUZFUTSGSPRIYNGMKDIPRCFSQJEGCHEXBVMPGTQMGGROOESIMTMIAUTTJFWPNVTKBBWLSRRCJRJOMBPRHQOVTUPKWNDUIARNXDDHBINJOTWADDJNUNCMGYXWWVMYITYYWNPJMFCDMYEDSQFUPWMGCAWZLBVLWINBAECVMOTCSAREMSPZMUTDQZOAQQPNDLWCFUOLKIDQBQWNIZBSNSXDGMPWUZBFVQITEFMKUHENUULAPBLXLE'
    chave_usada = 2

    mensagem_descriptografada = descriptografarMensagem(mensagem_criptografada, chave_usada)
    #armazena a mensagem descriptografada pela função de descriptografia em uma variável.

    print("Mensagem descriptografada:", mensagem_descriptografada)

    pyperclip.copy(mensagem_descriptografada)

def descriptografarMensagem(texto_cifrado, chave):
    #esta função simula a grade utilizada para descriptografar a cifra de transposição, representando as linhas, colunas e elementos excluidos da grade.

    colunas = math.ceil(len(texto_cifrado) / chave)
    linhas = chave
    elementos_excluidos = (linhas * colunas - len(texto_cifrado))

    mensagem = [''] * colunas #cada string da lista representa uma coluna.
    coluna = 0
    linha = 0

    for caractere in texto_cifrado:
        #iterendo sobre cada caractere da mensagem criptografada, cada caractere será destinado a sua respectiva culuna.

        mensagem[coluna] += caractere

        coluna += 1 #pula para a próxima coluna

        if coluna == colunas or (linha >= linhas - elementos_excluidos and coluna == colunas - 1):
            #se todas as colunas estiverem sido preenchidas ou se a coluna atual encontra um elemento excluído, pula para a próxima linha.
            
            coluna = 0
            linha += 1

    return ''.join(mensagem) #junta as strings da lista e retorna uma única string que é a mensagem descriptografada.

if __name__ == '__main__':
    main()
