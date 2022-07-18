from gestor_turnos.turn import Turn
from gestor_turnos.client import Client
from gestor_turnos.vehicle import Vehicle

choice = -1


def check_input(selection):
    if selection == 1:
        new_turn()
    if selection == 2:
        search_turn()
    if selection == 3:
        edit_turn()
    if selection == 4:
        delete_turn()
    if selection == 5:
        today()
    if selection == 6:
        exit()


def new_turn():
    print('creando un turno...')
    dat = input('ingrese la fecha del turno, formato hh:mm - dd:mm:aa ')
    nam = input("ingrese el nombre del Cliente: ")
    surn = input("ingrese el apellido del Cliente: ")
    doc = input("ingrese el DNI del Cliente: ")
    bra = input("ingrese la Marca del vehiculo: ")
    mod = input("ingrese el Modelo del vehiculo: ")
    pla = input("ingrese la Patente del vehiculo: ")

    mot = input('ingrese el motivo de ingreso')

    newclient = Client(nam, surn, doc)
    newvehicle = Vehicle(bra, mod, pla)
    newturn = Turn(dat, newclient, newvehicle, mot)

    print(newvehicle)
    print(newclient)
    print(newturn)
    # dat, newclient, newvehicle, mot)


def search_turn():
    print('buscando turno...')


def edit_turn():
    print('editando turno...')


def delete_turn():
    print('borrando turno...')


def today():
    print('buscando turnos de hoy...')


while 0 > choice < 6:
    print('''       Bienvenido al gestor de turnos.
        por favor, ingrese una opción
        1) Crear turno
        2) Buscar turno
        3) Editar turno
        4) Eliminar turno
        5) Ver los turnos del dia
        6) Salir''')
    sel = int(input())
    check_input(sel)
