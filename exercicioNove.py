quantidadeLitros = float(input("Quantos litros você quer abastecer? "))
tipo = input("Você quer abastecer gasolina (G) ou etanol (E)? Obs: use apenas as letras em maiúsculo. ")

if tipo == "G" or tipo == "g" :
    G = quantidadeLitros * 5.80
    print(f"O tipo que você escolheu foi gasolina! O valor a ser pago é {G}, pois você "
          f"abasteceu {quantidadeLitros}")
else:
    if tipo == "E" or tipo == "e":
        E = quantidadeLitros * 4.90
        print(f"O tipo que você escolheu foi etanol! O valor a ser pago é {E}, pois você "
          f"abasteceu {quantidadeLitros}")
    else:
        print("Escolha inválida")