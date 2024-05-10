class Candidato:
    def __init__(self, nome, partido, nome_vice, cargos_ocupados, idade):
        self.nome = nome
        self.partido = partido
        self.nome_vice = nome_vice
        self.cargos_ocupados = cargos_ocupados
        self.idade = idade

# Lista de candidatos fictícios
candidatos = [
    Candidato("João Silva", "Partido A", "Maria Oliveira", "Vereador", 45),
    Candidato("Ana Santos", "Partido B", "José Pereira", "Deputado Estadual", 38),
    Candidato("Pedro Souza", "Partido C", "Fernanda Lima", "Prefeito", 50),
    Candidato("Mariana Costa", "Partido D", "Carlos Rodrigues", "Vereador", 42),
    Candidato("Rafaela Pereira", "Partido E", "Paulo Santos", "Vice-prefeito", 48),
    Candidato("Carlos Oliveira", "Partido F", "Patrícia Silva", "Deputado Federal", 55),
    Candidato("Luiz Mendes", "Partido G", "Sandra Almeida", "Prefeito", 47),
    Candidato("Fernando Alves", "Partido H", "Cristina Oliveira", "Vereador", 41),
    Candidato("Aline Lima", "Partido I", "Marcos Santos", "Prefeito", 49),
    Candidato("Rodrigo Costa", "Partido J", "Carla Oliveira", "Vereador", 44)
]

# Função para buscar informações do candidato pelo número
def buscar_candidato(numero):
    for candidato in candidatos:
        if numero == candidatos.index(candidato) + 1:
            return candidato
    return None

# Programa principal
def main():
    print("Guia de Consulta de Candidatos a Prefeito")
    print("=========================================")
    numero = int(input("Digite o número do candidato: "))

    candidato = buscar_candidato(numero)

    if candidato:
        print("\nInformações do Candidato:")
        print("Nome:", candidato.nome)
        print("Partido:", candidato.partido)
        print("Nome do Vice:", candidato.nome_vice)
        print("Cargos Ocupados:", candidato.cargos_ocupados)
        print("Idade:", candidato.idade)
    else:
        print("Candidato não encontrado.")

if __name__ == "__main__":
    main()
