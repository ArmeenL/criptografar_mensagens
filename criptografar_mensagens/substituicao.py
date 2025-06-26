import random

# Conjunto de caracteres a serem usados
caracteres = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,;:-_!?@#$%^&*()[]{}<>/|\\+=")

caracteres_embaralhados = caracteres.copy()
random.shuffle(caracteres_embaralhados)

# Cria a chave de substituição
CHAVE = {}
for original, substituto in zip(caracteres, caracteres_embaralhados):
    CHAVE[original] = substituto

# Cria a chave reversa
CHAVE_REVERSA = {valor: chave for chave, valor in CHAVE.items()}


# Criptografar mensagem
def criptografar_mensagem(mensagem):
    resultado = ''
    for letra in mensagem.upper():
        if letra in CHAVE:
            resultado += CHAVE[letra]
        else:
            resultado += letra
    return resultado

# Descriptografar mensagem
def descriptografar_mensagem(mensagem):
    resultado = ''
    for letra in mensagem.upper():
        if letra in CHAVE_REVERSA:
            resultado += CHAVE_REVERSA[letra]
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