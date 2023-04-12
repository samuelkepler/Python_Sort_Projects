#Questão 3 

#Você deve desenvolver uma função para lidar com Strings em Python. Essa função deve receber como parâmetro uma string e uma letra que será procurada.

#Se o DIA do seu aniversário for um número PAR:
 #A função deve retornar a primeira posição da letra na String. Caso não seja encontrada, deve retornar -1.

#Se o DIA do seu aniversário for um número ÍMPAR:
 #A função deve retornar a quantidade de vezes que a letra aparece na String. Caso não seja encontrada, deve retornar -1.

#Após implementar a função, utilize-a para 5 valores digitados pelo usuário.

#----------------------------------------------------------------------------------

def findLetter(phrase, letter):
  counter = 0
  while counter < len(phrase):
    if (phrase[counter] == letter):
      return counter
    counter = counter+1

  return -1


for Lt in range(0,5):
  phrase = str(input("Digite uma frase de seu gosto: "))
  letter = str(input("Digite a letra a qual você quer procurar: "))
  print(findLetter(phrase,letter))
