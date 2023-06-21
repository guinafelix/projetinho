import random
import time
import matplotlib.pyplot as plt
plt.show()
from functools import reduce

import numpy as np
# e é o array que armazena o custo de entrada em cada linha
# a é o array de custo de cada estação
# t é o array de custo de troca de linha
# x é o array que armazena o custo de saída em cada linha

# a = [[4, 5, 3, 2, 4, 5, 3, 2], [2, 10, 1, 4, 4, 5, 3, 2]]
# t = [[0, 7, 4, 5, 7, 4, 5, 9], [0, 9, 2, 8, 9, 2, 8, 5]]
# e = [10, 12]
# x = [18, 7]
dictNormal = {}
dictGulao = {}
 
# ALGORITMO DE RESOLUÇÃO UTILIZANDO PROGRAMAÇÃO DINÂMICA
def fastestWayStation(a, t, e, x):
  startTime = time.time()
  NUM_STATION = len(a[0])
  T1 = [0 for i in range(NUM_STATION)]
  T2 = [0 for i in range(NUM_STATION)]
  line = [0 for i in range(NUM_STATION)]  # Armazena a linha escolhida em cada estação
  path = []  # Armazena o caminho percorrido
  
  T1[0] = e[0] + a[0][0]
  T2[0] = e[1] + a[1][0]
  
  for i in range(1, NUM_STATION):
    if T1[i-1] + a[0][i] <= T2[i-1] + t[1][i] + a[0][i]:
      T1[i] = T1[i-1] + a[0][i]
      line[i] = 1
    else:
      T1[i] = T2[i-1] + t[1][i] + a[0][i]
      line[i] = 2
    
    if T2[i-1] + a[1][i] <= T1[i-1] + t[0][i] + a[1][i]:
      T2[i] = T2[i-1] + a[1][i]
      line[i] = 2
    else:
      T2[i] = T1[i-1] + t[0][i] + a[1][i]
      line[i] = 1
  
  # Determinar o caminho percorrido
  lastLine = 1 if T1[NUM_STATION-1] + x[0] <= T2[NUM_STATION-1] + x[1] else 2
  path.append(lastLine)
  
  for i in range(NUM_STATION-1, 0, -1):
    lastLine = line[i]
    path.append(lastLine)
  
  path.reverse()
  
  endTime = time.time()  # Registra o tempo de término da execução
  executionTime = endTime - startTime
  # Retornar o valor mínimo e o caminho percorrido
  return min(T1[NUM_STATION-1] + x[0], T2[NUM_STATION-1] + x[1]), path, executionTime


# ALGORITMO DE RESOLUÇÃO UTILIZANDO GREEDY APPROACH
def greedyFastestWayStation(a, t, e, x):
  startTime = time.time()
  NUM_STATION = len(a[0])
  line = [0 for i in range(NUM_STATION)]  # Armazena a linha escolhida em cada estação
  path = []  # Armazena o caminho percorrido
  cost = 0  # Armazena o custo total da solução gulosa
  
  for i in range(1, NUM_STATION):
    if a[0][i] + t[0][i-1] <= a[1][i] + t[1][i-1]:
      line[i] = 1
      cost += a[0][i] + t[0][i-1]
    else:
      line[i] = 2
      cost += a[1][i] + t[1][i-1]
  
  # Adiciona o custo das estações finais
  cost += x[0] if e[0] + a[0][0] <= e[1] + a[1][0] else x[1]
  
  # Determinar o caminho percorrido
  lastLine = 1 if e[0] + a[0][0] <= e[1] + a[1][0] else 2
  path.append(lastLine)
  
  for i in range(1, NUM_STATION):
    lastLine = line[i]
    path.append(lastLine)

  path.reverse()
  endTime = time.time() # Registra o tempo de término da execução
  executionTime = endTime - startTime # Calcula o tempo de execução
  # Retornar o custo e o caminho percorrido
  return cost, path, executionTime

# Função para imprimir o resultado
def printStations(result, n): 
  print(f'custo total: {result[0]}')
  print(f'tempo de execução: {result[2]} segundos')
  print("Caminho percorrido:")
  for i in range(n): 
    print(f'Estação {i+1}, linha {result[1][i]}') 
  print()

# Execução dos algoritmos

# print(f'{10 * "-"} DYNAMIC PROGRAMMING APPROACH {10 * "-"}')
# result = fastestWayStation(a, t, e, x)
# printStations(result, len(result[1]))

# print(f'{10 * "-"} GREEDY APPROACH {10 * "-"}')
# greedyPath = greedyFastestWayStation(a, t, e, x)
# printStations(greedyPath, len(greedyPath[1]))


def geraVetor(n, var=0):
  array = []
  for i in range(0, n):
    if i == 0 and var == 1:
      array.append(0)
    array.append(random.randint(1, 10))
  return array


def teste():
  testes = 2
  for _ in range(1, 3):
    # n = random.randint(200000, 205000)
    n = random.randint(1, 3)
    while n in dictNormal.keys():
      # n = random.randint(200000, 205000)
      n = random.randint(1, 3)
    c = []
    d = []
    arrayNormal = []
    arraygulao = []
    for _ in range(1, testes):
      a = []
      t = []
      e = []
      x = []
      a.append(geraVetor(n))
      a.append(geraVetor(n))
      t.append(geraVetor(n, 1))
      t.append(geraVetor(n, 1))
      e = geraVetor(2)
      x = geraVetor(2)
      temponormal = fastestWayStation(a, t, e, x)
      tempogulao = greedyFastestWayStation(a, t, e, x)
      arrayNormal.append(temponormal[2])
      arraygulao.append(tempogulao[2])
    dictNormal[n] = reduce(lambda x, y: (x+y)/10, arrayNormal, 0)
    dictGulao[n] = reduce(lambda x, y: (x+y)/10, arraygulao, 0)
    c.clear()
    d.clear()
    arrayNormal.clear()
    arraygulao.clear()
  print(dictNormal)
  print(dictGulao)

teste()
xNormal = []
xGulao = []
yNormal = []
yGulao = []

def getXNormal(array):
  for key in array.keys():
    xNormal.append(key)

def getXGulao(array):
  for key in array.keys():
    xGulao.append(key)

def getYNormal(array):
  for key in array.keys():
    yNormal.append(array[key])

def getYGulao(array):
  for key in array.keys():
    yGulao.append(array[key])

getXNormal(dictNormal)
getXGulao(dictGulao)
getYNormal(dictNormal)
getYGulao(dictGulao)

fig, axes = plt.subplots(nrows=1, ncols=2,figsize=(12,2))

axes[0].plot(xNormal,yNormal,color="blue")
axes[0].set_xlabel('x dynamic approach')
axes[0].set_ylabel('y dynamic approach')

axes[1].plot(xGulao,yGulao,color="red")
axes[1].set_xlabel('x greedy approach')
axes[1].set_ylabel('y greedy approach')