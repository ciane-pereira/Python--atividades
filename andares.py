#Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.
#Escreva um código que imprima todos os números exceto o número 13. Escreva mais um código que resolva o mesmo problema, mas dessa vez usando o laço de repetição 'while'.
#Como desafio, imprima eles em ordem decrescente (20, 19, 18...)

andar = 21
print("Usando for na execução da atividade: \n")
for i in range(1,andar):  
  andar = andar + 1
  if(i == 13):
    continue
    if(andar == 21):
      break
  print("andar " + str(i) + " º")

print("\nUsando while na execução da atividade: \n")
andar = 20
while andar > 0:
    if(andar != 13):
        print("andar ",andar,"º" )
    andar = andar - 1
 