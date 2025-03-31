nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário: "))

print(f"Seu nome é {nome}, sua idade é {idade} e seu salário é {salario:.3F}")

aumento = float(input("Me informe o percentual de seu aumento: "))
percentual = (aumento/100) * salario
novoSalario = percentual + salario

print(f"Seu novo salário é {novoSalario:.3F} e seu aumento foi de {percentual:.2F}")


