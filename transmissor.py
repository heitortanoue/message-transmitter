from utils import *
from meiodecomunicacao import *

def aplicacaoTransmissora():
    mensagem = input("Digite uma mensagem: ")
    print()

    imprime_mensagem("Mensagem enviada pelo transmissor:", "yellow")
    print(mensagem)
    print()
    # Chama a próxima camada
    camadaAplicacaoTransmissora(mensagem)

def camadaAplicacaoTransmissora(mensagem: str):
    # Transforma a mensagem em uma lista de bits
    bits = string_para_bits(mensagem)

    imprime_mensagem("Mensagem enviada em bits:", "grey")
    imprime_bits(bits)
    print()

    # Chama a próxima camada
    camadaEnlaceDadosTransmissora(bits)

def controleErroEnlaceTransmissora(bits: list):
    escolha = TIPO_VERIFICACAO_ERRO

    imprime_mensagem("Verificação de erro escolhida:", "grey")
    if escolha == 1:
        imprime_mensagem("Paridade Par", "blue")
        return calcular_paridade_par(bits)
    elif escolha == 2:
        imprime_mensagem("Paridade Ímpar", "blue")
        return calcular_paridade_impar(bits)
    elif escolha == 3:
        imprime_mensagem("CRC-32", "blue")
        return calcular_CRC32(bits)
    else:
        imprime_mensagem("Sem verificação de erro")
        return bits

def camadaEnlaceDadosTransmissora(bits: list):
    # Controle de erros
    bits = controleErroEnlaceTransmissora(bits)

    print()
    imprime_mensagem("Mensagem enviada com bits de verificação de erro:", "grey")
    imprime_bits(bits, True)
    print()

    # Chama a próxima camada
    camadaFisicaTransmissora(bits)

def camadaFisicaTransmissora(bits: list):
    # Meio de comunicação
    bits = meioDeComunicacao(bits)