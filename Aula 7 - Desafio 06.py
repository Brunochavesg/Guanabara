n1 = float(input ("Quanto de dinheiro você tem na carteira? R$"))
tipo = input ("Você quer convertar para dolar ou euro?")
dolar = float(5.27)
if tipo == "DOLAR":
    print (f"Você tem R${n1} Reais e pode comprar US${n1/dolar:.2f} Dolar")
elif tipo == "EURO":
    print (f"Você tem R${n1} Reais e pode comprar EU${n1/dolar:.2f} Euro")
else:
    print ("Moeda desconhecida, digite dolar ou.")

