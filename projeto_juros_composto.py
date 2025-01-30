from math import pow

def composto(capital, juros, meses):
    return capital*pow((1+juros), meses)


capital = float(input("Digite o valor do capital Investido: "))
juros = float(input("Digite o percentual de juros ao mes: "))
meses = int(input("Digite a quantidade de meses que capital ficara investido: "))
juros = juros / 100


valor_final_composto = composto(capital, juros, meses)
print(f'O valor recebido ao final de {meses} meses e {valor_final_composto:.2f} R$' )
print(f'O valor total dos juros foi de {valor_final_composto - capital:.2f} R$')