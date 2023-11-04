# [CONSTANTES A SEREM DEFINIDAS]
# ============================

# TIPO_VERIFICACAO_ERRO = 1 -> Paridade Par
# TIPO_VERIFICACAO_ERRO = 2 -> Paridade Ímpar
# TIPO_VERIFICACAO_ERRO = 3 -> CRC-32
TIPO_VERIFICACAO_ERRO = 3

# PROBABILIDADE DE GERAR ERRO EM UM BIT DA MENSAGEM
PROBABILIDADE_ERRO = 1e-3

# Utilizado CRC-32 IEEE 802.3
POLINOMIO_CRC32 = 0xEDB88320

# ============================

from termcolor import colored

def string_para_bits (input_str: str):
    input_bytes = [format(ord(i), '08b') for i in input_str]
    bits = []
    for byte in input_bytes:
        for bit in byte:
            bits.append(int(bit))

    return bits


def string_para_bytes (input_str: str):
    input_bytes = input_str.encode('utf-8')
    return input_bytes


def bits_para_string (bits: list):
    input_bytes = []
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        input_bytes.append(byte)

    input_str = ""
    for byte in input_bytes:
        input_str += chr(int("".join([str(bit) for bit in byte]), 2))

    return input_str

def bits_para_array_bits (bits: str):
    array_bits = []
    for bit in bits:
        array_bits.append(int(bit))

    return array_bits

def imprime_bits(bits):
    """Imprime os bits em grupos de 8 bits"""
    for i in range(0, len(bits), 8):
        print("".join(map(str, bits[i:i+8])), end=" ")
    print()

def imprime_bits_colorido(bits, bits_certos):
    """Imprime os bits, colorindo os bits errados."""
    i = 0
    while i < len(bits):
        for j in range(min(8, len(bits) - i)):
            if bits[i+j] == bits_certos[i+j]:
                print(colored(bits[i+j], 'green'), end="")
            else:
                print(colored(bits[i+j], 'red'), end="")
        print(" ", end="")
        i += 8
    print()

def imprime_mensagem(mensagem, cor):
    """Imprime a mensagem com a cor especificada"""
    print(colored(mensagem, cor))


# FUNÇÕES DE CONTROLE DE ERRO DO TRANSMISSOR
# ============================
def calcular_paridade_par(bits):
    """Adiciona um bit de paridade par à lista de bits"""
    num_uns = sum(bits)
    # Se o número de uns for par, adiciona 0; caso contrário, adiciona 1
    bit_paridade = 0 if num_uns % 2 == 0 else 1
    bits.append(bit_paridade)
    return bits

def calcular_paridade_impar(bits):
    """Adiciona um bit de paridade ímpar à lista de bits"""
    num_uns = sum(bits)
    # Se o número de uns for ímpar, adiciona 0; caso contrário, adiciona 1
    bit_paridade = 1 if num_uns % 2 == 0 else 0
    bits.append(bit_paridade)
    return bits

def calcular_CRC32(bits: list):
    # Converte a lista de bits para uma lista de bytes.
    dados_em_bytes = string_para_bytes(bits_para_string(bits))

    # Inicializa o valor de CRC com um valor pré-definido.
    crc = 0xFFFFFFFF

    # Itera sobre cada byte dos dados.
    for c in dados_em_bytes:

        # Faz um XOR entre o CRC atual e o byte atual.
        crc ^= c

        # Itera sobre cada bit do byte.
        for _ in range(8):

            # Desloca o CRC para a direita em uma posição.
            # Se o bit menos significativo for 1, faz XOR com o polinômio.
            # Caso contrário, o CRC permanece o mesmo.
            crc = (crc >> 1) ^ (POLINOMIO_CRC32 * (crc & 1))

    # Inverte todos os bits do CRC final.
    crcCalculado = (crc ^ 0xFFFFFFFF) & 0xFFFFFFFF

    # Converte o CRC calculado em uma string binária de 32 bits.
    crcBinario = bin(crcCalculado)[2:].zfill(32)

    # Converte a string binária do CRC em uma lista de bits.
    crcListBinario = bits_para_array_bits(crcBinario)

    # Anexa o CRC ao final da mensagem original e retorna.
    return bits + crcListBinario


# FUNÇÕES DE CONTROLE DE ERRO DO RECEPTOR
# ============================
def verificar_paridade_par(bits):
    """Verifica a paridade par nos bits recebidos"""
    num_uns = sum(bits[:-1])
    bit_paridade = bits[-1]
    if num_uns % 2 == 0 and bit_paridade == 0:
        return bits[:-1], True
    elif num_uns % 2 == 1 and bit_paridade == 1:
        return bits[:-1], True
    else:
        return bits[:-1], False

def verificar_paridade_impar(bits):
    """Verifica a paridade ímpar nos bits recebidos"""
    num_uns = sum(bits[:-1])
    bit_paridade = bits[-1]
    if num_uns % 2 == 1 and bit_paridade == 0:
        return bits[:-1], True
    elif num_uns % 2 == 0 and bit_paridade == 1:
        return bits[:-1], True
    else:
        return bits[:-1], False

def verificar_crc32(bits_recebidos):
    """Verifica se o CRC-32 dos bits recebidos está correto."""
    mensagem_recebida_sem_crc = bits_recebidos[:-32]

    mensagem_com_crc_calculado = calcular_CRC32(mensagem_recebida_sem_crc)

    crc_calculado = mensagem_com_crc_calculado[-32:]
    crc_recebido = bits_recebidos[-32:]

    if crc_recebido == crc_calculado:
        return (mensagem_recebida_sem_crc, True)
    else:
        return (mensagem_recebida_sem_crc, False)
