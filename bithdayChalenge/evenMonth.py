#Question 2

#Make a program that reads two arrays of size 100 of integers, then creates a list with the sum of the elements of each array. 
#So that the first number is the sum of the first number of the two vectors, and so on for the entire vector. Right away:

#If your birthday MONTH is an even number:
#Display the first 50 numbers of the resulting array.

#If your birthday MONTH is an ODD number:
#Display the last 50 numbers of the resulting array.

#------------------------------------------------ -------------------------------------------

#I need to generate two arrays with random, with 100 integers, create a third array to receive the sum of these two arrays, where sum will be the first number 
#of array one with the first number of the array two (sum of indices), then ask it to show the sum of the first 50 numbers (0 - 49), a bubble or a logical 
#binary search.

import random


import numpy as np

lista1 = [np.random.randint(300,800, (100))]
lista2 = [np.random.randint(100,500, (100))]
produtoLista = []


for linhas in range(len(lista1)):
  for colunas in range(len(lista1[linhas])):
    sumListas = lista1[linhas][colunas] + lista2[linhas][colunas]
    produtoLista.append(sumListas)


for i in range (0,int(len(produtoLista)/2)):
  print(f"O {i + 1}º número da lista: {produtoLista[i]}")



print(f"Esta é sua primeira lista:  {lista1}")


print(f"Esta é sua segunda lista:  {lista2}")


print(f"Esta é a soma das suas duas listas:  {produtoLista}")
