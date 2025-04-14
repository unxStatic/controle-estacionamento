class Estacionamento:
    def __init__(self, total_vagas):
        # Inicializa o estacionamento com um número total de vagas
        self.total_vagas = total_vagas
        self.vagas_ocupadas = 0

    def adicionar_carro(self):
        # Tenta adicionar um carro ao estacionamento
        if self.vagas_ocupadas < self.total_vagas:
            self.vagas_ocupadas += 1
            print(f"Carro adicionado. Vagas ocupadas: {self.vagas_ocupadas}/{self.total_vagas}")
        else:
            print("Estacionamento cheio! Não há vagas disponíveis.")
    
    def remover_carro(self):
        # Tenta remover um carro do estacionamento
        if self.vagas_ocupadas > 0:
            self.vagas_ocupadas -= 1
            print(f"Carro removido. Vagas ocupadas: {self.vagas_ocupadas}/{self.total_vagas}")
        else:
            print("Não há carros no estacionamento para remover.")
    
    def vagas_livres(self):
        # Retorna o número de vagas livres
        vagas_livres = self.total_vagas - self.vagas_ocupadas
        print(f"Vagas livres: {vagas_livres}/{self.total_vagas}")
        return vagas_livres

# Exemplo de uso
estacionamento = Estacionamento(20)  # Estacionamento com 20 vagas

# Adicionando e removendo carros
estacionamento.adicionar_carro()  # Adiciona um carro
estacionamento.adicionar_carro()  # Adiciona outro carro
estacionamento.remover_carro()    # Remove um carro

# Exibindo vagas livres
estacionamento.vagas_livres()
