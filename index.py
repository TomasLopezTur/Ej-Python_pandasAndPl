from dates.db.index import db
from dates.plot.index import plot

df = db()

print ('Bienvenidos a NBA All Star')
def menu():
    select= input('Ingrese que desea ver:\nA.Ver todos los jugadores \nB.Detalle por jugador \nC.Ver puntaje general \nD.Graficar jugadores \nE.Salir\n').upper()
    if select == 'A':
        verN()
        input('\n(Presione Enter para ir al menu...)')
        menu()
    elif select == 'B':
        detail()
        input('\n(Presione Enter para ir al menu...)')
        menu()
    elif select == 'C':
        mediaJ()
        input('\n(Presione Enter para ir al menu...)')
        menu()
    elif select == 'D':
        plot()
        input('\n(Presione Enter para ir al menu...)')
        menu()
    elif select == 'E':
        op = input('Estas seguro qe deseas salir: Y/N \n').upper()
        if op == 'Y':
            input('Gracias por su visita!!!\n(Presione Enter para seguir...)')
            exit()
        elif op == 'N':
            menu()
        else:
            input('La opcion seleccionada no es correcta \n(Presione Enter para seguir...)')
            menu()
    else:
        input('La opcion seleccionada no es correcta \n(Presione cualquier tecla para seguir...)')
        menu()

def verN():
    for i in df.nombre:
        print(i)

def detail():
    nameD = input('Ingrese el nombre del jugador:\n').lower()
    player = df[df['nombre'] == nameD]
    if not player.empty:
        print(player)
    else:
        print(f'No se encontraron jugadores con el nombre de {nameD}.')

def mediaJ():
    long =len(df.puntos)
    suma = 0
    for i in df.puntos:
        suma = suma + i
    media = suma/long
    print(f'La media de los puntos de los jugadores es:  {media:.2f}.')


input('Presiona Enter para comenzar...\n')
menu()
""" print(df) """