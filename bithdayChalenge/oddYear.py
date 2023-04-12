#Questão 1 (2,5 pontos)

#Desenvolva um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 
#(que não deve ser armazenado). Após esta entrada de dados, faça:

#Se o ano do seu aniversário for um número PAR:
 #Mostre a quantidade de valores que foram lidos;
 #Exiba todos os valores na ordem decrescente em que foram informados;
 #Calcule e mostre a soma dos valores;

#Se o ano do seu aniversário for um número ÍMPAR:
 #Calcule e mostre a média dos valores;
 #Calcule e mostre a quantidade de valores acima da média calculada;
 #Calcule e mostre a quantidade de valores abaixo de 7;
#--------------------------------------------------------------------------------------------------------------

todosVal = []
numbers = 0 

while (numbers != -1):
   numbers = float(input("digite os números de seu desejo: "))
   todosVal.append(numbers)

#retirada do -1
todosVal.pop()

def mediaLista (lista):
  media = sum(lista)/len(lista)
  return media

#variavel que recebe o valor da média
mediaF = mediaLista(todosVal)

def acimaMedia (lista, media):
  listaPmedias = []

  for i in range(len(lista)):
    if (lista[i] > media ):
      listaPmedias.append(lista[i]) 
  return listaPmedias

#variavel que recebe os valores a cima da media
AcMedias = acimaMedia(todosVal, mediaF)

def baixoSete (lista):
  listaB7 = []

  for i in range(len(lista)):
    if (lista[i] < 7 ):
      listaB7.append(lista[i]) 
  return listaB7

#variavel que recebe os valores a baixo de 7
abSete = baixoSete(todosVal)
   

#print dos valores digitados  
print(f"Valores digitados pelo usuarios:  {todosVal}")  

#print da media da lista
print(f"Média dos valores inseridos na lista:  {mediaF}")

#print dos valores acima da media da lista
print(f"Aqui estão todos os valores a cima da média da lista:  {AcMedias}")

#print dos valores a baixo de 7
print(f"Aqui estão todos os valores abaixo do valor 7, pertencentes a lista:  {abSete}")

