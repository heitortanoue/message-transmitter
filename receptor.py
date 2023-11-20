from utils import *

def camadaFisicaReceptora(bits: list, bits_corretos: list):
    imprime_mensagem("Mensagem recebida com bits de verificação de erro:", "grey")
    imprime_bits_colorido(bits, bits_corretos)
    print()

    # Chama a próxima camada
    camadaEnlaceDadosReceptora(bits)

def controleErroEnlaceReceptora(bits: list):
    escolha = TIPO_VERIFICACAO_ERRO

    bitsVerificados = []
    correto = False

    if escolha == 1:
        bitsVerificados, correto = verificar_paridade_par(bits)
    elif escolha == 2:
        bitsVerificados, correto = verificar_paridade_impar(bits)
    elif escolha == 3:
        bitsVerificados, correto = verificar_crc32(bits)
    else:
        bitsVerificados = bits

    return bitsVerificados, correto

def camadaEnlaceDadosReceptora(bits: list):
    # Controle de erros
    bits, correto = controleErroEnlaceReceptora(bits)

    if not correto:
        imprime_mensagem("[ERRO DETECTADO!]\n", "red")
    else:
        imprime_mensagem("Nenhum erro detectado na transmissão!\n", "green")

    imprime_mensagem("Mensagem recebida em bits:", "grey")
    imprime_bits(bits)
    print()

    # Chama a próxima camada
    camadaAplicacaoReceptora(bits)

def camadaAplicacaoReceptora(bits: list):
    # Transforma a lista de bits em uma string
    mensagem = bits_para_string(bits)

    # Chama a próxima camada
    aplicacaoReceptora(mensagem)

def aplicacaoReceptora(mensagem: str):
    imprime_mensagem("Mensagem recebida pelo receptor:", "yellow")
    print(mensagem)
    print()
