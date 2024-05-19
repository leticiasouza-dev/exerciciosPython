'''2.	O usuário deve inserir sua idade, e o programa deverá classificá-lo em uma das seguintes categorias: 
"Criança" (até 12 anos), 
"Adolescente" (13 a 17 anos), 
"Adulto" (18 a 64 anos) e 
"Idoso" (65 anos ou mais).

Etapas de realização:
•	Solicitar a idade do usuário;
•	Utilizar estruturas de seleção para determinar a categoria com base na idade;
•	Exibir a categoria correspondente à idade do usuário.'''

idade = int(input("Digite sua idade: "))

if idade <= 12:
    print("Você é uma criança")

elif idade >= 13 and idade <= 17:
    print("Você é um adolescente")

elif idade >= 18 and idade <= 64:
    print("Você é um adulto")

else:
    print("Você é um idoso")


