http://axon.cs.byu.edu/~randy/jair/wilson2.html

Os testes estão sendo feitos até uma distância de 2 pixels

Euclidiana:
Notável que o algoritmo passa primeiro pelos pixels que vem abaixo para depois subir e passar pela próxima coluna
Ele calcula primeiramente a coluna (de baixo para cima) e quando não há mais dados para se pegar ele passa para a outra coluna coletando os dados
Isto foi observado em um teste em que o algoritmo calculava a distancia euclidiana de 4 pixels
O resultado do experimento foi algo parecido com isto:
[0, 0] = [187, 255] , [152, 255] = 35
[0, 1] = [234, 255] , [130, 255] = 104
[1, 0] = [212, 255] , [29, 255] = 183
[1, 1] = [172, 255] , [98, 255] = 74

O que � estranho � que a segunda parte da formula da distancia euclidiana sempre vai dar 0, j� que subtrai 255 com 255.
A pr�xima etapa � verificar se isto esta realmente certo sobre dar sempre 0 e fazer o algoritmo somar os valores do resultado.

Mahalanobis:
Utiliza desvio padrão para uma análise mais precisa
A minha implementanção ainda não foi testada

Manhatan:
Se for apenas um |x1 - x2| + |y1 - y2| meu algoritmo esta correto.
Problema encontrado é o de que imagens iguais não vão se anular, ou seja, o resultado de suas distancias não será 0

---

Testes com Filtros:
Distancia Euclidiana:
SEM FILTRO: 225.84
SHARPEN: 216.22
DETAIL: 216.06
EDGE_ENHANCE: 228.59
EDGE_ENHANCE_MORE: 231.97
