import random
from receptor import camadaFisicaReceptora
from utils import PROBABILIDADE_ERRO

def meioDeComunicacao(bits):
    """Simula o meio de comunicação, podendo introduzir erros nos bits transmitidos."""

    # Definindo a probabilidade de erro para cada bit (por exemplo, 10%)
    probabilidade_erro = PROBABILIDADE_ERRO

    # Para cada bit, verifica se ocorrerá um erro
    bits_transmitidos = []
    for bit in bits:
        if random.random() < probabilidade_erro:
            # Inverte o bit se ocorrer um erro
            bits_transmitidos.append(1 if bit == 0 else 0)
        else:
            bits_transmitidos.append(bit)

    # Próxima camada (que já é o receptor)
    camadaFisicaReceptora(bits_transmitidos, bits)
