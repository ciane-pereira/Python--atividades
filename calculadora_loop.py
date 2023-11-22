## Função Calculadora -loop

#Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:

#1: Soma
#2: Subtração
#3: Multiplicação
#4: Divisão
#0: Sair

#Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

#Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar.

#É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado. 

#Definição das operações
def calculadora(num1, num2, operacao):
  if(operacao == 1):
    return num1 + num2    
  elif(operacao == 2):
    return num1 - num2   
  elif(operacao == 3):
    return num1 * num2   
  elif(operacao == 4):
    if(num2 != 0):
      return num1 / num2      
    else:
      print("Não é possível dividir por zero.")     
  else:     
      return 0

#Execução das operações
calculadora_operando = True
while(calculadora_operando == True): 
  operacao = int(input("Escolher a operação:\n 1: Soma\n 2: Subtração\n 3: Multiplicação\n 4: Divisão\n 0: Sair\n"))
  if(operacao < 0 or operacao > 4):
    print("Essa opção não existe\n")
  elif(operacao == 0):
    calculadora_operando = False
  else:
    num1 = int(input("\n Digitar um número: "))
    num2 = int(input("Digitar outro número: "))     

  resultado = calculadora(num1, num2, operacao)
  print(f"O resultado da operação é: {resultado}\n")   