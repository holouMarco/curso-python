#Ejercicio bucle while
#Fase 1

# number = 9
# humanNumber = input('Introduce un numero del 1 al 10, si aciertas ganas')

# while number != int(humanNumber):

#     humanNumber = input('Intentalo de nuevo ')

# print('Has ganado')

#Fase 2

number = 9
counter = 0
opoLeft = 0
humanNumber = input('Introduce un numero del 1 al 10, si aciertas ganas.Solo tienes 3 intentos mas.\n')

while counter < 3:

    if int(humanNumber) > 0 and int(humanNumber) <= 10:
        
        if number == int(humanNumber):

            print('Has ganado')
            break

        else:
            opoLeft = 3 - counter

            print(f'Te quedan {opoLeft} intentos')

            humanNumber = input('Intentalo de nuevo ')

            counter += 1
    
    else:
        print('Introduce un numero entre 1 y 10.')
        humanNumber = input('Intentalo de nuevo en el rango correcto ')
        counter += 1

print('Te has quedado sin intentos.')
