import math
import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do jogo
total_bolas = 75  # Total de bolas no bingo
bolas_marcadas = 24  # Bolas que cada jogador precisa para vencer (k)
num_jogadores = 29  # Número de jogadores
num_jogos = 1000  # Número de jogos simulados

# Função para calcular a probabilidade hipergeométrica para um único jogador
def probabilidade_individual(x):
    if x < bolas_marcadas + 1:
        return 0  # Não há possibilidade de vencer com menos bolas que o necessário
    return math.comb(x - 1, bolas_marcadas - 1) / math.comb(total_bolas, bolas_marcadas)

# Valores possíveis de X (número de bolas sorteadas)
X = np.arange(1, total_bolas + 1)

# Calculando a probabilidade para cada número de bolas sorteadas
prob_individual = np.array([probabilidade_individual(x) for x in X])

# Calculando a probabilidade de pelo menos um jogador vencer (jogo terminar)
prob_conjunta = 1 - (1 - prob_individual) ** num_jogadores




plt.bar(X, prob_conjunta, color='blue', alpha=0.6, label="Histograma Teórico")
plt.title("Histograma Teórico: 10.000 Jogos com 100 Jogadores")
plt.xlabel("Número de Bolas Sorteadas")
plt.ylabel("Frequência")
plt.legend()
plt.show()
