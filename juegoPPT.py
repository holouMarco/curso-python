# random es una de las multiples librerías que nos puede proporcionar python.
# choice es una funcionalidad de esta librería que escoge un elemento aleatorio
# Por lo tanto, importamos choice y obtendrá un elemento aleatorio de opciones(Eso será nuestro oponente)

from random import choice

opciones = ['piedra', 'papel', 'tijera']

# Creamos una variable que valdrá una elección aleatoria de opciones
eleccionOrdenador = choice(opciones)

# Dado ya nuestro oponente. Crea el juego ----piedra, papel, tijera----
# Se deben utilizar condicionales y operadores lógicos.
# En cada condición cumplida hay que printear el mensaje de empate, victoria o derrota

eleccionJugador = input('Haz tu eleccion: ')

if eleccionOrdenador == 'piedra' and eleccionJugador == 'tijera':
    print('El ordenador gana')

elif eleccionOrdenador == 'tijera' and eleccionJugador == 'papel':
    print('El ordenador gana')

elif eleccionOrdenador == 'papel' and eleccionJugador == 'piedra':
    print('El ordenador gana')

elif eleccionOrdenador == 'piedra' and eleccionJugador == 'papel':
    print('El jugador gana')

elif eleccionOrdenador == 'tijera' and eleccionJugador == 'piedra':
    print('El jugador gana')

elif eleccionOrdenador == 'papel' and eleccionJugador == 'tijera':
    print('El jugador gana')

else:
    print('Es un empate')

print('Ordenador:', eleccionOrdenador)
print('Jugador:', eleccionJugador)
