### Propostio do código
Irei discutir todas as particularidades sobre a aplicação pratica desse código em um post do medium.

## Cálculo do Número Total de Combinações de Cartelas

### 1. Número de combinações por coluna
Cada coluna contém 5 números únicos escolhidos de um intervalo específico:

- **Coluna B:** 
  $
  \binom{15}{5}
  $

- **Coluna I:** 
  $
  \binom{15}{5}
  $

- **Coluna N:** 
  $
  \binom{15}{4}
  $
  *(4 números porque o centro é livre)*

- **Coluna G:** 
  $
  \binom{15}{5}
  $

- **Coluna O:** 
  $
  \binom{15}{5}
  $

### 2. Número total de combinações para a cartela
Multiplicamos as combinações possíveis de cada coluna:

$
\text{Total de cartelas} = \binom{15}{5} \times \binom{15}{5} \times \binom{15}{4} \times \binom{15}{5} \times \binom{15}{5}
$

#### Substituindo os valores:

##### Cálculo de: $\binom{15}{5}$:

$
\binom{15}{5} = \frac{15!}{5!(15-5)!} = \frac{15 \times 14 \times 13 \times 12 \times 11}{5 \times 4 \times 3 \times 2 \times 1} = 3003
$

##### Cálculo de $\binom{15}{4}$:
$
\binom{15}{4} = \frac{15!}{4!(15-4)!} = \frac{15 \times 14 \times 13 \times 12}{4 \times 3 \times 2 \times 1} = 1365
$

#### Total:
$
\text{Total de cartelas} = 3003 \times 3003 \times 1365 \times 3003 \times 3003 = 111.007.923.832.370.565
$
