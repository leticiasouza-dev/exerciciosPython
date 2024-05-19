'''1.	 O programa deve gerar um número aleatório entre 1 e 100 e pedir ao usuário para adivinhá-lo. A cada palpite, o programa deverá informar se o número secreto é maior ou menor que o palpite. O jogo termina quando o usuário acerta o número, e o programa deverá informar o número de tentativas realizadas.
Etapas de realização:
•	Importar o módulo random;
•	Gerar um número aleatório entre 1 e 100;
•	Pedir repetidamente ao usuário para adivinhar o número, até que ele acerte;
•	A cada palpite, informar se o número é maior ou menor;
•	Ao acertar, mostrar o número de tentativas e terminar o jogo.'''

import random;

numero_aleatorio = random.randint(1,100);

print(numero_aleatorio);

palpite = int(input("Digite o seu palpite"));
tentativas = 1

while palpite != numero_aleatorio:
        if palpite < numero_aleatorio:
            print("O numero aleatório é maior que", palpite);
            

        else:
            print("O numero aleatório é menor que", palpite);
            

        palpite = int(input("Digite o seu palpite: "));
        tentativas += 1;

if palpite == numero_aleatorio:
    print("Parabéns você acertou o numero aleatório com", tentativas, "tentativas");
