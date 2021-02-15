#Ejercicio:

#Crea una estructura de control que determine que beben segun su edad
#Si tiene menos de 18 beben zumito
#Si tienen 18 beben tequila
#Si tienen mas de 18, beben cerveza
#Y sino, el valor no es correcto
#EN CADA CONDICION HAY QUE PRINTEAR UN MENSAJE DE LO QUE BEBEN

edad = input('Que edad tienes: ')
edad = int(edad)

if edad < 18:
    print('Solo puedes beber zumito de naranja')
elif edad == 18:
    print('Te puedo servir un chupito de tequila')
elif edad > 18:
    print('Como ya eres mayor te puedo dar una buena jarra de cerveza')
else:
    print('La edad introducida no corresponde a ninguna de este universo, vuelva a intentar')
    
# Revisa si edad es un digito
edad = input('Que edad tienes: ')

# Este if revisa si el input es un digito

if edad.isdigit():
    edad = int(edad)
else:
    print('Para tu conocimiento la edad es un numero no untexto. Ponlo bien anda')
    edad = int(input('Que edad tienes: '))

if edad < 18:
    print('Solo puedes beber zumito de naranja')
elif edad == 18:
    print('Te puedo servir un chupito de tequila')
elif edad > 18:
    print('Como ya eres mayor te puedo dar una buena jarra de cerveza')
else:
    print('La edad introducida no corresponde a ninguna de este universo, vuelva a intentar')
