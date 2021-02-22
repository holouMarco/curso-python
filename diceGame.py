import random

# Cualquier nombre de variable y/o función debe estár en ingles

# JUEGO DE LOS DADOS. Mayor puntuación GANA!!

# Crea una función que reciba 2 argumentos: El dado de da_chuck y holou



# Dentro de la función debe printear un mensaje de que número le ha tocado a cada uno


# Crea un bloque condicional que compruebe si ha habido empate, victoría o derrota y devuelva el mensaje

def diceRoll(option1, option2):

    print(f'Player 1 number is {option1}')
    print(f'Player 2 number is {option2}')

    if option1 == option2:

        return 'Player 1 and Player 2 draw'

    elif option1 > option2:

        return 'Player 1 win'

    else:

        return 'Player 2 win'

# Dado de da_chuck (número aleatorio del 1 al 9, ambos incluidos)
diceDaChuck = random.randint(1, 9)

# Dado de Holou (número aleatorio del 1 al 9, ambos incluidos)
diceHolou = random.randint(1, 9)

# Llamada a la función

result = diceRoll(diceDaChuck, diceHolou)

# Printea el resultado de la función

print(result)
