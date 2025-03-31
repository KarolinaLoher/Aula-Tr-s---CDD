notaUm = float(input("Digite sua primeira nota: "))
notaDois = float(input("Digite sua segunda nota: "))
notaTres = float(input("Digite sua terceira nota: "))

media = (notaUm + notaDois + notaTres) / 3

if media>=7 :
    print("Parabéns! Você foi aprovado!")
else:
    if media < 4:
        print("Você foi reprovado")
    else:
        print ("Você está de recuperação")

