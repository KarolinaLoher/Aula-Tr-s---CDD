timeUm = input("Digite o nome do seu time: ")
golsUm = int(input("Digite a quantidade de gols que o time um fez: "))
timeDois = input("Digite o nome do seu time: ")
golsDois = int(input("Digite a quantidade de gols que o time dois fez: "))

if golsUm>golsDois :
    print(f"O time {timeUm} venceu!")
else:
    if golsUm<golsDois :
        (f"O time {timeDois} venceu!")
    else :
        print("Empate!")