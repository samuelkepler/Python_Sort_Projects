#Questão 4

#Desenvolva um programa que armazene quatro notas em uma lista e que apresente a média final. Caso a média seja igual ou superior a 7, apresentar a mensagem "APROVADO", 
#caso contrário, armazenar a nota da prova final e recalcular a média. A nova média será calculada entre a média anterior e a nota da prova final. 
#Caso a nova média seja igual superior a 5, apresentar a mensagem "APROVADO", caso contrário, apresentar a mensagem "REPROVADO".

#------------------------------------------------------------------------------------------------------------------------------------------------------------

notas = []

for iNotas in range(0,4):
  iNotas = float(input("digite as notas em sequência: "))
  notas.append(iNotas)
  print(notas)

sumNotas = sum(notas)/len(notas)

if ( sumNotas >=7 ):
    print("aluno aprovado com ",sumNotas )
    
elif (sumNotas < 7 ):
  provaFinal = float(input(" Digite a média da final "))
  mediaFinal =  (sumNotas + provaFinal)/2
  
  if (mediaFinal >= 5 ):
    print("aluno Aprovado com ",sumNotas)
  
  elif (mediaFinal < 5 ):
    print("aluno reprovado com ",sumNotas)



 
