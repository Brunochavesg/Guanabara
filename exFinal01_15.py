#Exercicios Finais de aula 01 a 15
print ("**Olá! Seja Bem vindo ao Exercicio**")
nome = input("Qual o seu nome:? ")
print (f"Olá {nome}!")
idade = int(input("Me informe a sua idade: "))
print (f"Você tem {idade} anos.")
dia = int(input("Qual o dia que você nasceu:? "))
mes = input("Qual o mes? (Ex. Março, Setembro.)")
ano = int(input("Qual o ano? (Ex. 1999):"))
print (f"Você nasceu dia {dia} de {mes} do ano de {ano}.")
sal_ini = float(input("Qual seu salário? R$"))
sal_mes = float(input("Quantos Meses você trabalho com esse Salário?"))
print (f"Seu sálario inicial foi R${sal_ini:.2f} e somando todos os meses você ganhou R${sal_ini * sal_mes:.2f}")
real = float(input("Digite um valor em Real: R$"))
print (f"Com R${real} reais voce consegue comprar US${real / 4.90:.2f}")



