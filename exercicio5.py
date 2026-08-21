lado1= int(input("digite o primeiro lado do triangulo:"))
lado2= int(input("digite o segundo lado do triangulo:"))
lado3= int(input("digite o terceiro lado do triangulo:"))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
  if lado1==lado2==lado3:
     print(" triangulo equilatero")
  elif lado1==lado2 or lado1==lado3 or lado2==lado3
     print("triangulo isoceles.")
e



else:
    print(" Os lados não formam um triangulo. ")
