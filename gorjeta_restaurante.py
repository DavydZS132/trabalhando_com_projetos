# João trabalha como garçom em um restaurante e precisa calcular a gorjeta que os clientes deixam ao pagar a conta. O restaurante sugere uma gorjeta de 10%, mas alguns clientes podem escolher dar mais ou menos.

# Para agilizar o processo, João quer um programa que receba o valor total da conta e a porcentagem de gorjeta desejada e exiba o valor final que o cliente deverá pagar.

# Crie um programa que peça ao usuário o valor da conta e a porcentagem de gorjeta. O programa deve calcular e exibir o valor da gorjeta e o total a ser pago.

# Exemplo de entrada:

# Digite o valor da conta: 120.00  
# Digite a porcentagem de gorjeta: 10  

# Saída esperada:

# Valor da gorjeta: R$ 12.00  
# Total a pagar: R$ 132.00

# resultado = valor * (1 - (porcentagem / 100)) Calculo
def calculo_gorjeta(valor_da_conta_calculo, porcentagem_gorjeta_calculo):

    return valor_da_conta_calculo * (porcentagem_gorjeta_calculo / 100)
    

valor_da_conta = float(input('Digite o valor da conta: '))

while True:
    porcentagem_gorjeta = float(input('Digite a porcentagem de gorjeta: '))

    if porcentagem_gorjeta >= 10:
        break
    else:
        print('O valor da gorjeta tem que ser de 10% ou maior.')

calculo = calculo_gorjeta(valor_da_conta, porcentagem_gorjeta)

resultado = valor_da_conta + calculo

print(f'Valor da gorjeta: {calculo:.2f} \nTotal a pagar: {resultado:.2f}')