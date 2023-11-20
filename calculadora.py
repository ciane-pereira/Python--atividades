#Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
#1- Soma
#2- Subtração
#3- Multiplicação
#4- Divisão
#Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

def calculadora(num1, num2, operacao):
  if(operacao == 1):
    return num1 + num2
    print(resultado)
  elif(operacao == 2):
    return num1 - num2
    print(resultado)
  elif(operacao == 3):
    return num1 * num2
    print(resultado)
  elif(operacao == 4):
    if(num2 != 0):
      return num1 / num2      
    else:
      print("Não é possível dividir por zero.")
      return 0
  else:
      print("Operação inválida. Escolha 1: Soma, 2: Subtração, 3: Multiplicação, 4: Divisão.")
      return 0

num1 = float(input("Digitar um número: "))
num2 = float(input("Digitar outro número: "))     
operacao = int(input("Escolher a operação (1: Soma, 2: Subtração, 3: Multiplicação, 4: Divisão): "))

resultado = calculadora(num1, num2, operacao)
print("O resultado da operação é: ", resultado)   