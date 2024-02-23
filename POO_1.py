import random

# Ideas:
# Añadir un mínimo de monedas (si has recogido 3 monedas bien, si no vuelve a recogerlas)
# En algunas rooms, que se tenga que adivinar un num aleatorio. While not encontrado, no pasa. <<HECHO>>
# Que tu aparición en las habitaciones sea aleatoria (pero que si vuelves atrás, que vuelvas a empezar en la misma) <<HECHO>>

'''
<Desplazamientos definidos>
#1. Unidireccionales
Portal azul celeste: desván ---> bedroom_1
Portal rosa: south_hall ---> desván
Portal verde chillón: ladder ---> parking
Portal marrón: contadores ---> floor_2
Portal granate: bedroom_1 ---> azotea
Portal marrón: floor_2 ---> parking

#2. Bidireccionales
Portal amarillo: bedroom_2 <---> contadores
Portal morado: dining_room <---> parking
Portal rojo: kitchen <---> pool
Portal azul: floor_1 <---> fountain
Portal gris: floor_3 <---> ladder
Portal negro: bedroom_2 <---> azotea

#3. Aparcamiento
Como se puede subir a dos lugares distintos, lo decidirá un randint.
Las opciones serán 7 (fuente) u 8 (piscina).
'''

class Room:
    '''
    Inicializamos la clase "Room", con la que crearemos las habitaciones.
    Esta clase tiene un constructor, con 6 atributos.
    '''
    def __init__(self, description, north, east, south, west, num):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.num = num


class Jardin(Room):
    '''
    Subclase de la clase "Room".
    '''
    def __init__(self, description, north, east, south, west, num):
        super().__init__(description, north, east, south, west, num)

class Plantas(Room):
    '''
    Subclase de la clase "Room"
    '''
    def __init__(self, description, north, east, south, west, num):
        super().__init__(description, north, east, south, west, num)

class Extra(Room):
    '''
    Subclase de la clase "Room".
    '''
    def __init__(self, description, north, east, south, west, num):
        super().__init__(description, north, east, south, west, num)

def comprobar_apuesta(intentos, current_room, aux):
    '''
    Vamos a comprobar que la apuesta que hace el usuarios (a adivinar el número secreto para abrir la puerta) es correcto.
    Tenemos 3 intentos, si los agotamos volveremos al punto en el que comenzamos la partida.
    Si acertamos, termina el juego :)
    '''
    error = True
    done = False
    numero_aleatorio = random.randint(0, 5)
    apuesta = int(input("Oh no, you've found a door which is unlocked with a random number between 0 and 5 (both included). \nCan you unlock the door, please? (You have only 3 lives):  "))
    while intentos > 1:
        intentos -= 1
        if numero_aleatorio == apuesta:
            print("The door has been unlocked! You have reached the balcony. Congrats!!!")
            done = True
            error = False
            break

        else:
            apuesta = int(input(f"NOPE. Try again please, you still have {intentos} attempts left:  "))

    if error == True:
        print("I'm so sorry... you are back to where you started")
        current_room = aux
    return done, current_room

def main():
    # Jardín
    fountain = Jardin("near the fountain", 12, None, 9, None, 7)
    parking = Jardin("in the parking", 7, None, None, 2, 9)
    pool = Jardin("near the swimming pool", 5, None, 9, None, 8)
    ladder = Jardin("near the ladder", 9, 10, None, 6, 13)

    # Plantas
    floor_1 = Plantas("in the 1st floor", 7, 7, 11, 11, 12)
    floor_2 = Plantas("in the 2nd floor", None, 9, None, 10, 11)
    floor_3 = Plantas("in the 3rd floor", 13, 11, 11, 13, 10)

    # Extra
    terrace_room = Extra("in the terrace room", 0, None, None, None, 14)
    meter_room = Extra("in the meter room", 0, None, 11, None, 15)
    storage_room = Extra("in the storage room", None, None, 3, None, 16)

    # Parte interna
    bedroom_2 = Room("in the Bedroom 2", None, 1, 15, 14, 0)
    bedroom_1 = Room("in the Bedroom 1", 14, None, None, None, 3)
    north_hall = Room("in the North Hall", 6, None, 1, None, 4)
    kitchen = Room("in the Kitchen", None, 8, None, None, 5)
    dining_room = Room("in the Dining Room", None, 9, None, 1, 2)
    south_hall = Room("in the South Hall", 4, 2, 16, 0, 1)
    balcony = Room("in the Balcony", None, None, 4, None, 6)

    # Lista con todas las zonas
    room_list = [bedroom_2, south_hall, dining_room, bedroom_1, north_hall, kitchen, balcony, fountain, pool, parking,
                 floor_3, floor_2, floor_1, ladder, terrace_room, meter_room, storage_room]
    current_room = random.randint(0, 16)
    aux = current_room

    #Saludo y explicación del juego
    nombre = input("What's up? Which is your name?\n")
    print(f"Hello, {nombre}! \nIn this game you are going to spawn in a random room, and you'll have to find out where the\nbalcony is.")
    print(f"You'll be able to move to the north (n), south (s), east (e) and west (w).")
    print(f"When you reach the balcony the game will finish. Can you beat it?")

    #Juego como tal
    done = False
    while not done:
        intentos = 3 #Inicializamos los intentos
        error = True #error será True por defecto, si acertamos será False.

        next_room_north = room_list[current_room].north
        next_room_west = room_list[current_room].west
        next_room_south = room_list[current_room].south
        next_room_east = room_list[current_room].east

        '''
        De las clases, cogeremos qué habitaciones están al norte, oeste, sur, este (si hay).
        '''

        direccion = input(f"\nOk {nombre}... You are {room_list[current_room].description}, where do you want to go? (n, s, e, w): ")
        if direccion.lower() == "n" or direccion.lower() == "north":
            if next_room_north == 6:
               done, current_room = comprobar_apuesta(3, current_room, aux)

            elif current_room == 9:
                next_room_north = random.randint(7, 8)
                current_room = next_room_north
            else:
                if next_room_north == None:
                    print("You can't go that way.")
                elif next_room_north == 6:
                    print("You have reached the balcony. Congrats!!!")
                    done = True
                else:
                    current_room = next_room_north
        elif direccion.lower() == "w" or direccion.lower() == "west":
            if next_room_west == 6:
                done, current_room = comprobar_apuesta(3, current_room, aux)

            elif next_room_west == None:
                print("You can't go that way.")
            else:
                current_room = next_room_west
        elif direccion.lower() == "s" or direccion.lower() == "south":
            if next_room_south == 6:
                done, current_room = comprobar_apuesta(3, current_room, aux)

            elif next_room_south == None:
                print("You can't go that way.")
            else:
                current_room = next_room_south
        elif direccion.lower() == "e" or direccion.lower() == "east":
            if next_room_east == 6:
                done, current_room = comprobar_apuesta(3, current_room, aux)

            elif next_room_east == None:
                print("You can't go that way.")
            else:
                current_room = next_room_east
        else:
            '''
            El programa solo entiende n, s, e, w.
            Si metemos otro carácter nos hablará en un idioma extraterrestre y nos pedirá de nuevo otro carácter.
            '''
            print("No entchiendo andalu' illo, sholo' (n, s, e, w).")

if __name__ == "__main__":
    main()
