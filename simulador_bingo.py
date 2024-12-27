from  bingo import CartelaBingo,VerificadorBingo
import random
import matplotlib.pyplot as plt
import pandas as pd

vb = VerificadorBingo()
def simular_bingo(numero_jogos):
    """
    função que simula um bingo e devolve quantas bolas foram necessarias para vencer equantos vencedores tiveram
    """
    cartelas_jogos = {}
    for i in range(numero_jogos):
        a = CartelaBingo()
        cartelas_jogos[a] = False
        
    bolas = [i+1 for i in range(75)]

    for i in range(75):
        index_sorteio = random.randint(0,len(bolas)-1)
        sorteada = bolas.pop(index_sorteio)
        for jogo in cartelas_jogos.keys():
            jogo.preencher(sorteada)
            cartelas_jogos[jogo] = vb.cheia(jogo)

        if any(cartelas_jogos.values()):
            row = [i,len([key for key, value in cartelas_jogos.items() if value])]
            return row

linhas = []
n = 10000
p = 1000
for i in range(n):
    linhas.append(simular_bingo(p))

df = pd.DataFrame(linhas,columns=["n_bolas",'n_ganhadores'])

plt.hist(df['n_bolas'], bins="auto", edgecolor='black', alpha=0.7)
plt.title(f'Histograma de Números de bolas até vitória | {n} jogos analisados com {p} participantes ')
plt.xlabel('Número de Bolas')
plt.ylabel('Frequência')
plt.show()