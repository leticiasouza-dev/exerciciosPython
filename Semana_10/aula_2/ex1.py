'''1.	Desenvolva um programa que peça ao usuário para criar uma senha. O programa deve verificar se a senha atende a critérios específicos (por exemplo, pelo menos 8 caracteres, contendo números e letras). Se a senha não atender aos critérios, o programa deve pedir ao usuário para tentar novamente. Utilize um laço de repetição e expressões booleanas para validar a senha.

Orientações:
•	Peça ao usuário para inserir uma senha;
•	Use um laço while para repetir a solicitação até que a senha atenda aos critérios;
•	Defina expressões booleanas para verificar se a senha tem o comprimento adequado e se contém os caracteres necessários;
•	Se a senha não atender aos critérios, informe o usuário e peça uma nova tentativa.'''

print("----- BEM-VINDO  AO SISTEMA PARA CRIAÇÃO DE SENHAS-----")

senha = str(input("Digite uma senha"))

while len(senha) < 8:
    print("A senha deve conter 8 caracteres")

    senha = str(input("Digite uma senha"))

    
if len(senha) >= 8: print("Senha criada com sucesso");