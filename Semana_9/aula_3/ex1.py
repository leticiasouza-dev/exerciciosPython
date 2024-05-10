class ElementoQuimico:
    def __init__(self, sigla, numero_atomico, nome, massa):
        self.sigla = sigla
        self.numero_atomico = numero_atomico
        self.nome = nome
        self.massa = massa

# Lista de elementos químicos
elementos_quimicos = [
    ElementoQuimico("H", 1, "Hidrogênio", 1.008),
    ElementoQuimico("He", 2, "Hélio", 4.0026),
    ElementoQuimico("Li", 3, "Lítio", 6.94),
    ElementoQuimico("Be", 4, "Berílio", 9.0122),
    ElementoQuimico("B", 5, "Boro", 10.81),
    ElementoQuimico("C", 6, "Carbono", 12.011),
    ElementoQuimico("N", 7, "Nitrogênio", 14.007),
    ElementoQuimico("O", 8, "Oxigênio", 15.999),
    ElementoQuimico("F", 9, "Flúor", 18.998),
    ElementoQuimico("Ne", 10, "Neônio", 20.180),
    # Adicione mais elementos aqui
]

# Função para buscar informações do elemento químico pela sigla
def buscar_elemento(sigla):
    for elemento in elementos_quimicos:
        if sigla.lower() == elemento.sigla.lower():
            return elemento
    return None

# Programa principal
def main():
    print("Consulta de Elementos Químicos")
    print("==============================")
    sigla = input("Digite a sigla do elemento químico: ")

    elemento = buscar_elemento(sigla)

    if elemento:
        print("\nInformações do Elemento Químico:")
        print("Sigla:", elemento.sigla)
        print("Número Atômico:", elemento.numero_atomico)
        print("Nome:", elemento.nome)
        print("Massa:", elemento.massa)
    else:
        print("Elemento químico não encontrado.")

if __name__ == "__main__":
    main()
