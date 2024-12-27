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
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Scatter Plot')
plt.show()
