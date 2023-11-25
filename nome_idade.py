# Introdução tratamento de Erros(Try/ Except)
##Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2022.
##A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2023).

##Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.


#nome completo com verificação de uso somente de letras
while True:
    try:
        print('Escreva seu nome completo:')
        nome = input()
        
        if nome.replace(" ", "").isalpha():
            print('Seu nome completo é: ' , nome)
            break
        else:
            print('Erro na digitação! Digite somente letras.')
    except:
        print('Ocorreu um erro')

#digitar ano de nascimento e verificar se condições do período definito são cumpridas  
while True:   
    try:
        print('Digite seu ano de nascimento:')
        ano = int(input())

        if (ano < 1922) or (ano > 2022):
            print("Ano de nascimento dever ser entre 1922 e 2022.")            
        else:
            idade = 2023 - ano
            print('Seu nome é ', nome, 'e sua idade é ', idade, 'anos')
            break
    except:
        print('digite número válido.')