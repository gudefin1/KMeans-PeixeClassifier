import random as random

#funçao para calcular a distancia entre 2 pontos
def calcular_distancia(p1,p2):
    return sum((p - q) ** 2 for p,q in zip(p1, p2)) ** 0.5

#função para calcular o centro de um cluster --> media aritimetica
def calcular_centro(c):
    return[sum(valores) / len(valores) for valores in zip(*c)]

#dados disponiveis para treinamento

peixes = [
            [70, 4], [68, 3.8], [40, 2], [35, 1.9], 
            [71, 3.9], [69, 3.9], [41, 2.5], [36, 1.7], 
            [73, 4.1], [70, 3.8], [40, 2], [38, 2.1], 
            [69, 3.8], [71, 3.9], [41, 2.2], [39, 2.4] 
        ]
# numero de clusters
k = 2

#inicalizar o centro dos klusters
centro = random.sample(peixes, k)

#treinamento dos centros
for _ in range(len(peixes)):
    cluster = {i: [] for i in range(k)}


    #atribuiçao dos dados durante o treinamento
    for p in peixes:
        distancia = [calcular_distancia(p, x)for x in centro]
        index =  distancia.index(min(distancia))       
        cluster[index].append(p)
        print(cluster)
    
    #atualização do valor do centro de cada cluster
    novo_centro = [calcular_centro(c) for c in cluster.values()]

    if all(calcular_distancia(novo_centro[i], centro[i]) < 0.001 for i in range(k)):
        break

        centro = novo_centro

#imprimir resultado

print(f"centro dos clusters: {centro} ")
print(f"clusters: {cluster}")
print()


#################################################################################################
#testando o algoritimo com um elemento que nao estava no treinamento

novo_objeto = [94, 12]

#calcula a distancia entre o novo OBJ e cada centro de cada cluster

distancia_ = [calcular_distancia(novo_objeto, c) for c in centro]

#encontra o indice do centro com a menor distancia
index = distancia.index(min(distancia))

#impressao do numero do cluster qual o novo objeto pertence
print(index)