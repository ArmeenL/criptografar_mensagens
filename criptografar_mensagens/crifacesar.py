import random

# Conjunto de caracteres a serem usados
CARACTERES = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,;:-_!?@#$%^&*()[]{}<>/|\\+=")
TAMANHO_CARACTERES = len(CARACTERES)

# Criando chave aleatória
CHAVE = random.randint(3, 10)


# Criptografar mensagem
def criptografar_mensagem(mensagem):
    resultado = ""
    for letra in mensagem.upper():
        if letra in CARACTERES:
            index = CARACTERES.index(letra)
            nova_letra = CARACTERES[(index + CHAVE) % TAMANHO_CARACTERES]
            resultado += nova_letra
        else:
            resultado += letra
    return resultado

# Descriptografar mensagem
def descriptografar_mensagem(mensagem):
    resultado = ""
    for letra in mensagem.upper():
        if letra in CARACTERES:
            index = CARACTERES.index(letra)
            nova_letra = CARACTERES[(index - CHAVE) % TAMANHO_CARACTERES]
            resultado += nova_letra
        else:
            resultado += letra
    return resultado

# ------------------ EXEMPLO DE USO ------------------ #
mensagem = "Mensagem secreta!"

cifrada = criptografar_mensagem(mensagem)
print(f'Mensagem original: {mensagem}')
print(f'Mensagem criptografada: {cifrada}')
print("-"*50)
decifrada = descriptografar_mensagem(cifrada)
print(f'Mensagem descriptografada: {decifrada}')