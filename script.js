// Inicialize as variáveis
let totalVagas = 20;  // Altere aqui para o número total de vagas
let vagasOcupadas = 0;

// Função para atualizar o display das vagas
function atualizarVagas() {
    const vagasLivres = totalVagas - vagasOcupadas;
    document.getElementById('vagas-ocupadas').textContent = vagasOcupadas;
    document.getElementById('vagas-livres').textContent = vagasLivres;
    document.getElementById('total-vagas').textContent = totalVagas; // Atualiza o total de vagas na página
}

// Função para adicionar um carro
function adicionarCarro() {
    if (vagasOcupadas < totalVagas) {
        vagasOcupadas++;
        atualizarVagas();
    } else {
        alert("Estacionamento cheio! Não há vagas disponíveis.");
    }
}

// Função para remover um carro
function removerCarro() {
    if (vagasOcupadas > 0) {
        vagasOcupadas--;
        atualizarVagas();
    } else {
        alert("Não há carros no estacionamento para remover.");
    }
}

// Chama a função para inicializar a página com o número de vagas
atualizarVagas();

