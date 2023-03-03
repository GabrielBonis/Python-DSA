#PSEUDOCODIGO 2:
#INICIE
#PRINTE NA TELA: "BEM VINDO À CALCULADORA DO BONIS"
#PERGUNTE AO USUÁRIO QUAL OPERAÇÃO MATEMÁTICA SERÁ UTILIZADA (+, -, *, /) ARMAZENE A RESPOSTA COMO UMA VARIÁVEL
#PERGUNTE AO USUÁRIO QUAL O PRIMEIRO NUMERO Á SER USADO NA OPERAÇÃO ARMAZENE A RESPOSTA COMO UMA VARIÁVEL
#PERGUNTE AO USUÁRIO QUAL O SEGUNDO NUMERO À SER USADO NA OPERAÇÃO ARMAZENE A RESPOSTA COMO UMA VARIÁVEL
#TESTE QUAL O VALOR UTILIZADO (+, -, *, /)
#REALIZE A CONTA: VARIAVEL PRIMEIRO NUMERO VARIÁVEL OPERAÇÃO VARIÁVEL SEGUNDO NUMERO
#PRINTE NA TELA O RESULTADO

print('Bem vindo a Calculadora')

operacao = input('Qual operação matemática a ser utilizada? (utilize: +, -, *, /)')

valor_1 = float(input('Qual o primeiro valor'))
valor_2 = float(input('Qual o segundo valor'))

if(operacao == "+"):
  resultado = valor_1 + valor_2

elif(operacao == "-"):
  resultado = valor_1 - valor_2

elif(operacao == "*"):
  resultado = valor_1 * valor_2

elif(operacao == "/"):
  resultado = valor_1 / valor_2

print(resultado)