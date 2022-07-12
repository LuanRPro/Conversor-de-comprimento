# CONVERSOR DE MEDIDAS DE COMPRIMENTO

#Declaração de variáveis

medidas = ['MM', 'C', 'M']
valor = 0
milimetrosCentimetros = 0
milimetrosMetros = 0
centimetrosMilimetros = 0
centimetrosMetros = 0
metrosCentimetros = 0
metrosMilimetros = 0

# Primeira entrada do usuário

primeiraMedida = input('Informe a medida atual do valor que você deseja converter utilizando (MM) para milímetros, (C) para centímetros ou (M) para metros: ')

# Verifica se a medida escolhida é válida

while primeiraMedida not in medidas :

    print('\nEntrada inválida, apenas (MM), (C) e (M) são permitidos (maiúsculos).\n\n Tente de novo:\n\n')
    primeiraMedida = input('Informe a medida atual do valor que você deseja converter utilizando (MM) para milímetros, (C) para centímetros ou (M) para metros: ')

# Uma vez que a primeira medida foi escolhida corretamente, continua

else :

# Segunda entrada do usuário

    segundaMedida = input('Informe a medida para a qual você deseja converter o valor utilizando (MM) para milímetros, (C) para centímetros ou (M) para metros: ')

# Verifica se a medida escolhida é válida

    while segundaMedida not in medidas :

        print('\nEntrada inválida, apenas (MM), (C) e (M) são permitidos (maiúsculos).\n\n Tente de novo:\n\n')
        segundaMedida = input('Informe a medida para a qual você deseja converter o valor utilizando (MM) para milímetros, (C) para centímetros ou (M) para metros: ')

# Verifica se o valor recebido é válido

    while True :

        try :
            valor = float(input('Informe o valor a ser convertido: '))
    
        except :
            ValueError(print('\n***ERRO***\n\nApenas números são permitidos! Tente de novo:\n\n'))
            continue

        else :
            break

# Fórmulas

    milimetrosCentimetros = valor / 10
    milimetrosMetros = valor / 1000
    centimetrosMilimetros = valor * 10
    centimetrosMetros = valor / 100
    metrosCentimetros = valor * 100
    metrosMilimetros = valor * 1000

# Milimetros para Centimetros
    if primeiraMedida == 'MM' and segundaMedida == 'C' :
        print('\n{} mm é igual a {:.3f} cm'.format(valor, milimetrosCentimetros))

# Milimetros para Metros
    elif primeiraMedida == 'MM' and segundaMedida == 'M' :
        print('\n{} mm é igual a {:.3f} m'.format(valor, milimetrosMetros))

# Centimetros para Metros
    elif primeiraMedida == 'C' and segundaMedida == 'M' :
        print('\n{} cm é igual a {:.3f} m'.format(valor, centimetrosMetros))

# Centimetros para Milimetros
    elif primeiraMedida == 'C' and segundaMedida == 'MM' :
        print('\n{} cm é igual a {:.3f} mm'.format(valor, centimetrosMilimetros))

# Metros para Centimetros
    elif primeiraMedida == 'M' and segundaMedida == 'C' :
        print('\n{} m é igual a {:.3f} cm'.format(valor, metrosCentimetros))

# Metros para Milimetros
    elif primeiraMedida == 'M' and segundaMedida == 'MM' :
        print('\n{} m é igual a {:.3f} mm'.format(valor, metrosMilimetros))

# Se as medidas forem iguais
    else :
        print('\nA medida escolhida ({}) foi a mesma, {} é igual a {}'.format(primeiraMedida, valor, valor))