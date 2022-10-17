#Questão 2 

#Faça um programa que leia dois arrays de tamanho 100 de números inteiros, em seguida, crie uma lista com a soma dos elementos de cada array. De forma que o primeiro número seja a soma do primeiro número dos dois vetores, e assim sucessivamente para o vetor inteiro. Em seguida:

#Se o MÊS do seu aniversário for um número PAR:
#Exiba os 50 primeiros números do array resultante.

#Se o MÊS do seu aniversário for um número ÍMPAR:
#Exiba os 50 últimos números do array resultante.

#--------------------------------------------------------------------------------------------

#preciso gerar dois arrays com random, com 100 numeros inteiros, criar um terceiro array para receber a soma desses dois arrays, onde soma vai ser o primerio numero do array um
#com o primerio numero do array dois ( soma de  indices), depois pedir que ele mostre a soma dos primerios 50 numeros ( 0 - 49), um bubble ou uma busca binaria a logica.
#Professor Gionvanni lhe mandei um modelo de bubble diferente do sue em aula, mas estudei por ele, espero que lembre disso pq ta no telegram, talvez use este modelo, 
#por acahar mai pratico.

import random

#aprendi este comando com uma professora de python no ensino médio
import numpy as np

lista1 = [np.random.randint(300,800, (100))]
lista2 = [np.random.randint(100,500, (100))]
produtoLista = []


for linhas in range(len(lista1)):
  for colunas in range(len(lista1[linhas])):
    sumListas = lista1[linhas][colunas] + lista2[linhas][colunas]
    produtoLista.append(sumListas)

#lista dos 50 primerios Arrays
for i in range (0,int(len(produtoLista)/2)):
  print(f"O {i + 1}º número da lista: {produtoLista[i]}")


#lista 1 criada e demonstrada
print(f"Esta é sua primeira lista:  {lista1}")

#lista 2 criada e demonstrada
print(f"Esta é sua segunda lista:  {lista2}")

#Soma da lista 1 e 2 demonstrada
print(f"Esta é a soma das suas duas listas:  {produtoLista}")
