"""
# Calcule  a soma dos numeros do 10 ao 14
Numeros = ([10, 11, 12, 13, 14])
soma = sum(Numeros)
print(soma)

# Calcule a media entre os numeros 10, 15, 20.
Numeros2 = ([10, 15, 20])
media = sum(Numeros2)/3
print(media)

# Peca para o usuario digitar duas notas de zero a dez e os pesos das notas e calcule a media ponderada entre elas
nota1 = int(input('Digite a nota 1: '))
peso1 = int(input('Agora digite o peso que essa nota tem: '))
nota2 = int(input('Digite a nota 2: '))
peso2 = int(input('Agora digite o peso que essa nota tem: '))
mediaDasNotas = int((nota1*peso1+nota2*peso2)/(peso1*peso2))
print(mediaDasNotas)


# Qual o menor preco da lista
precos = [100.20, 34.90, 31.50, 18.95]
menorPreco = min(precos)
print(f'O menor preco da lista informada e: R${menorPreco}')

# Faca um programa que recebe do usuario duas notas de zero a dez e escreva na tela "voce esta aprovado",
#se a media das duas notas for maior que 7

nota1 = int(input('Insira a primeira nota: '))
nota2 = int(input("Insira a segunda nota: "))
media = int((nota1+nota2)/2)
print(media)
if media >= 7:
    print("Voce esta aprovado")
elif media >= 5 and media < 7:
    print("Voce esta de exame")
else:
    print("Voce esta reprovado")


numero = 0
while numero <= 10:
    print(numero)
    numero += 1

numero_max = eval(input("Digite o numero max: "))
numero = 0
while numero <= numero_max:
    print(numero)
    numero += 1



for dia in ['segunda', 'terca', 'quarta', 'quinta', 'sexta']:
    print(dia, end=", ")

for numero in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print(numero, end=" ")

for numero in range(6):
    print(numero, end=" ")

for numero in range(5,51,5):
    print(numero, end=" ")



#Faca um exercicio que calcule o fatorial de um numero, fornecido pelo usuario. Exemplo: cinco fatorial 5! = 5*4*3*2*1

numero = int(input("Digite o fatorial desejado: "))
fatorial = numero
while numero >= 2:
    fatorial = fatorial * (numero - 1)
    numero -= 1
print(fatorial)



senha = "000"
tentativas = 3

while tentativas != 0:
    tentativa = input("Digite uma senha numerica: ")
    if tentativa == senha:
        print("Senha Correta, acesso concedido")
        break

    else:
        print("Senha Incorreta, tente novamente")
        tentativas -= 1
        if tentativas == 0:
            print("Acesso Bloqueado")

"""

# faca um programa que gere a tabuada correspondente ao numero digitado pelo usuario

tabuada = int(input("Digite o numero que deseja saber a tabuada: "))
limite = int(input("Ate qual numero sera mostrado?: "))

for numero in range(0, limite +1):
    print(f"{tabuada} X {numero} = {tabuada*numero}")