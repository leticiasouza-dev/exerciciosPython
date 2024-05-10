'''2.	Desenvolva um programa que implemente um jogo de adivinhação de números. O programa deve gerar um número 
aleatório entre 1 e 50 e pedir ao usuário para adivinhar esse número. No entanto, o usuário tem um limite de 
5 tentativas para acertar. O laço while deve ser usado para controlar as tentativas e fornecer feedback se o 
palpite está correto ou não. Se o usuário errar após 5 tentativas, o programa deve informar que o jogo acabou 
e revelar o número secreto.'''

import random

numeroAleatorio = random.randint(1,50)
print("BEM VINDO AO JOGO DE ADIVINHAÇÃO")
print("--------------------------------")

numeroTentativas = 0
limiteTentativas = 5

while numeroTentativas < limiteTentativas:
    numeroDigitado = int(input("Digite seu palpite: "))

    if numeroDigitado == numeroAleatorio:
        print("parabéns você acertou o numero secreto que era", numeroAleatorio)
        break

    elif numeroDigitado < numeroAleatorio:
        print("O numero secreto é maior que", numeroDigitado)

    else:
        print("O numéro secreto é menor que", numeroDigitado)

    
    numeroTentativas += 1

if numeroTentativas == limiteTentativas:
    print("Suas 5 tentativas acabaram. O número secreto era:", numeroDigitado)
