import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
"""
prorama para "simular" multiplos ogos e frequencia de vencedores

"""

total_bolas = 75  # Total de bolas no bingo
bolas_marcadas = 24  # Bolas que cada jogador precisa para vencer (k)
num_jogadores = 29  # Número de jogadores
num_jogos = 1000  # Número de jogos simulados

#função que é identica a vista no estat_bingo
def probabilidade_individual(x):
    if x < bolas_marcadas + 1:
        return 0 
    return math.comb(x - 1, bolas_marcadas - 1) / math.comb(total_bolas, bolas_marcadas)

#prob de pelomneos um vencedor 
X = np.arange(24, total_bolas + 1)
prob_individual = np.array([probabilidade_individual(x) for x in X])
prob_conjunta = 1 - (1 - prob_individual) ** num_jogadores


#irei randomizar um numero de 0-1 se for menor q a prob o jogador anha e plotamos
linhas = []
for i in range(num_jogos):
    aleatorio = np.random.rand()
    for j,k in enumerate(prob_conjunta):
        if k>aleatorio:
            linhas.append([j,1])
            break

df = pd.DataFrame(linhas,columns=["n_bolas",'n_ganhadores'])
plt.hist(df['n_bolas'], bins="auto", edgecolor='black', alpha=0.7)
plt.title(f'Histograma de Números de bolas até vitória | {num_jogos} jogos analisados com {num_jogadores} participantes ')
plt.xlabel('Número de Bolas')
plt.ylabel('Frequência')
plt.show()
        



quit()
plt.bar(X, prob_conjunta, color='blue', alpha=0.6, label="Histograma Teórico")
plt.title("Probabilidde de pelo menos um ogador vencer")
plt.xlabel("Número de Bolas Sorteadas")
plt.ylabel("Frequência")
plt.legend()
plt.show()
