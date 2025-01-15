import math
import random


class CartelaBingo:

    def __init__(self):
        self.cartela = {"B":[],"I":[],"N":[],"G":[],"O":[]}
        self.cartela_falsa = {chave: [False] * 5 for chave in ["B", "I", "N", "G", "O"]}
        self.cartela_falsa["N"][2] = True
        self.criar_cartela()

    def criar_cartela(self):
        self.cartela["B"] = random.sample(range(1, 16), 5)
        self.cartela["I"] = random.sample(range(16, 31), 5)
        n = random.sample(range(31, 46), 4)
        self.cartela["N"] = n[:2] + [0] + n[-2:]
        self.cartela["G"] = random.sample(range(46, 61), 5)
        self.cartela["O"] = random.sample(range(61, 76), 5)

    def __str__(self):
        
        resultado = []
        resultado.append(" B   |  I   |  N   |  G   |  O  ")
        resultado.append("-" * 29)
        for i in range(5):
            linha = []
            for coluna in "BINGO":
                valor = self.cartela[coluna][i] if len(self.cartela[coluna]) > i else " "
                linha.append(f"{valor:^5}")
            resultado.append("|".join(linha))
        resultado.append("-" * 29)
        return "\n".join(resultado)
    
    def preencher(self,sorteado):
        div = math.floor((sorteado-1)/15)
        try:
            index = self.cartela["BINGO"[div]].index(sorteado) 
            self.cartela_falsa["BINGO"[div]][index] = True
        except Exception as e:
            pass



class VerificadorBingo():

    def linha(self, linha_index):
        for coluna in self.cartela_falsa.values():

            if coluna[linha_index] is not True: 
                return False
        return True

    def coluna(self, coluna_letra):
        for valor in self.cartela_falsa[coluna_letra]:
            if valor is not True:  
                return False
        return True

    def diagonal(self, cartela_falsa):
        diagonal1 = all(
            cartela_falsa[coluna][i] is True for i, coluna in enumerate("BINGO")
        )
        diagonal2 = all(
            cartela_falsa[coluna][4 - i] is True for i, coluna in enumerate("BINGO")
        )
        return diagonal1 or diagonal2

    def cheia(self,cartela:CartelaBingo):
        return   all(all(value_list) for value_list in cartela.cartela_falsa.values())


if __name__ == "__main__":
    a = CartelaBingo()
    
    vb = VerificadorBingo()
    
    for i in range(76):
        j = int(input("valor sorteado"))
        a.preencher(j)
        print(a.cartela_falsa)
        if vb.cheia(a):
            print("ganhou")
            break

    

