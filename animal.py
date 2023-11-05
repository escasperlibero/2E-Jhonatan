class AnimalDeEstimacao:
    def __init__(self, nome, raca, idade, nome_responsavel, telefone_responsavel):
        self.nome = nome
        self.raca = raca
        self.idade = idade
        self.nome_responsavel = nome_responsavel
        self.telefone_responsavel = telefone_responsavel

    def __str__(self):
        return f"Nome: {self.nome}\nRaça: {self.raca}\nIdade: {self.idade}\nResponsável: {self.nome_responsavel}\nTelefone: {self.telefone_responsavel}"

def cadastrar_animal():
    nome = input("Nome do animal: ")
    raca = input("Raça do animal: ")
    idade = input("Idade do animal: ")
    nome_responsavel = input("Nome do responsável: ")
    telefone_responsavel = input("Telefone do responsável: ")

    animal = AnimalDeEstimacao(nome, raca, idade, nome_responsavel, telefone_responsavel)
    return animal

# Exemplo de uso:
animal1 = cadastrar_animal()
print("\nCadastro do Animal de Estimação:")
print(animal1)
