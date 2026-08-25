valor = float (input("valor da conta:"))
pessoa = int (input("quantidade de pessoa:"))
taxa = input ("adiciona 10%? (s ou n):")
if taxa == "s":
    valor == valor + valor * 0.10
elif taxa == "n" :
    print ("sem taxa de 10%")
else:
    print ("Opção iválida! Desconsiderar taxa")
valor_por_pessoa = valor / pessoa 
print("==== Resumo da conta ====")
print (f"valor da conta = R$ {valor :.2f}")
print(f" valor por pessoa = R$ { valor_por_pessoa:.2f}")