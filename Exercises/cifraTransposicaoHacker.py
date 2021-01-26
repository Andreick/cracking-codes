#Programa hacker - Cifra de transposição

import string, pyperclip, detectarIngles, cifraTransposicaoDescriptografia

def main():
    mensagemEscolhida = "Wtdnhhh gaoie tenaI vgt we iworynau ogslsu  da rb icaobdaire nsn p i rrsnweaasiacy tlt bhliae.ycbc ,eoaY  uuormtsuea e akp wlerIolsa uy cdl,ptod einnrrc''efettae   lcilwltsiry  ki,wtet ah ersat e toaaa  nlnie l taeyi ts dm sdiatauokhymtei b.sna. .gb H.soSu. uombwt aei Intth'sthal e vlcrwi a.rnsn igt'Tn ithktc olekbsen ees w  .fipa iterAnhreug f tetetirhchssetrm   e abbeinoe sdocon baf'tsu te.sm neya   ntwl oeeae'acsrsc,eto   mwnfpooalutvil osdmrh aimycteohenui t?nt. eh NsiIo.nt, g' Tssbh. ee sc Ooabhmue,ess tetah  nit"
    
    mensagemHackeada = hackearTransposicao(mensagemEscolhida)

    if mensagemHackeada == None:
        print("\nFalha ao hackear a criptografia.")
    else:
        print('Mensagem hackeada:\n"%s"' %(mensagemHackeada))
        pyperclip.copy(mensagemHackeada)

def hackearTransposicao(mensagem):
    print("Hackeando...")
    
    for chave in range(1, len(mensagem)):
        print('Testando a chave #%d...' %(chave))
        
        textoDescriptografado = cifraTransposicaoDescriptografia.descriptografarMensagem(mensagem, chave)

        if detectarIngles.podeSerIngles(textoDescriptografado):
            print("\nPossível hack da criptografia:")
            print('Chave %d:\n"%s[...]"' %(chave, textoDescriptografado[:200]))
            resposta = input("\nDigite 'C' se concluído ou digite qualquer outra coisa para continuar hackeando: ")
            print()
            
            if resposta.strip().upper() == 'C':
                return textoDescriptografado

    return None

if __name__ == '__main__':
    main()
