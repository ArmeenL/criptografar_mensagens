# Criptografia Clássica com Python

Este projeto demonstra dois métodos clássicos de criptografia:
a **Cifra de César** e a **Criptografia por Substituição**. 
Ambos os algoritmos são implementados em Python de forma simples e didática.

## Cifra de César

A **Cifra de César** é uma técnica de criptografia por substituição simples. 
Cada letra do texto original é substituída por outra letra, deslocada um número fixo de posições no alfabeto.

### Exemplo
Com um deslocamento de **+3**:
Texto original: A B C D E
Texto cifrado: D E F G H

### Características
- Usa um valor fixo de deslocamento (chave).
- Apenas letras são transformadas.
- Fácil de decifrar por força bruta (25 possibilidades).

## Criptografia por Substituição

Na **criptografia por substituição**, cada letra do alfabeto é substituída por outra, definida por uma chave personalizada. Diferente da Cifra de César, não há um padrão fixo de deslocamento.

### Exemplo
Alfabeto normal: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Chave de troca: Q W E R T Y U I O P A S D F G H J K L Z X C V B N M
Texto original: HELLO
Texto cifrado: ITSSD

### Características
- Cada letra é trocada por outra segundo uma chave fixa.
- Mais segura que a Cifra de César, mas ainda vulnerável à análise de frequência.

---

## 💡 Objetivo

Este projeto foi criado com fins educacionais, para demonstrar de forma simples como funcionam dois algoritmos clássicos de criptografia.
