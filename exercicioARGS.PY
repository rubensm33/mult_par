def function (*args):
    acumulador = 1
    for number in args:
        acumulador *= number

    return acumulador

def par_impar (*args):
    for number in args:
        if number % 2 == 0:
            return print(f'{number} é par')
        else:
            return print(f'{number} é ímpar')

   


print(function(1,2,3,4))
par_impar(4)