import math
import matplotlib.pyplot as plt

x = []
y = []
total = 0
for i in range(24,76):
    x.append(i)
    probabilidade = math.comb(i-1,23)/math.comb(75,24)
    total += probabilidade
    y.append(probabilidade)
    
print(total)
plt.scatter(x, y, color='blue', marker='o')

# Add labels and a title
plt.ylabel('P(X)')
plt.xlabel('Nº Bolas')
plt.title('´Distribuição hipergeométrica')
plt.show()
