#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
import os, platform

# Function to clear screen:
def clear_screen():
    pc = platform.system()
    if pc == "Windows":
        os.system('cls')  # for Windows
    else:
        os.system('clear')  # for Linux/OS X
    return

# Function to pause till' key input:
def system_pause():
    print(input('Presione Enter para continuar...'))
    return

# Function decoratior for displaying function title:
def f_decorator(func):
   def func_wrapper(name):
       return '\n{:#<65}'.format('') + '\n#{:^63}#'.format(func(name)) + '\n{:#<65}'.format('')
   return func_wrapper

# Class QPART with all its functions and menus:
class QPART:
    """ QPART Software.
        (Statistical Termodynamics)

        Program designed to compute partition
        functions of systems with one or two atoms.
        """

    # Function name:
    tra = "Funcion de particion traslacional"
    vib = "Funcion de particion vibracional"
    rot = "Funcion de particion rotacional"
    ele = "Funcion de particion electronica"
    tot = "Funcion de particion total"

    # Set global const:
    h = 6.626e-34
    c = 2.997e10
    k = 1.380e-23
    NA = 6.022e23

    def __init__(self):
        # Constructor:
        self.main_screen()
        return

    def main_screen(self):
        # Print main screen:
        clear_screen()
        self.welcome_screen()
        self.display_menu()
        self.selection_from_menu()
        return

    def welcome_screen(self):
        # Welcome description:
        print('{:#<65}'.format(''))
        print('#{:^63}#'.format('Software de Termodinamica Estadistica'))
        print('#{:^63}#'.format('QPART'))
        print('{:#<65}'.format(''))
        print('#{:^63}#'.format('Programa disenado para el calculo'))
        print('#{:^63}#'.format('de funciones de particion'))
        print('#{:^63}#'.format('de sistemas con uno o dos atomos'))
        print('{:#<65}'.format(''))
        return

    def display_menu(self):
        print("\nPara salir del programa en cualquier momento, haga Ctrl-C.")
        system_pause()
        # Print menu
        print('\nMENU:')
        print("1) {0}".format(self.tra))
        print("2) {0}".format(self.vib))
        # print("3) {0}".format(self.rot))
        # print("4) {0}".format(self.ele))
        # print("5) {0}".format(self.tot))
        # print("6) Salir del programa")
        return

    def selection_from_menu(self):
        from_menu = {1:self.qtraslacional, 2:self.qvibracional}
        #, 3:self.qrotacional, 4:self.qelectronica, 5:qtotal, 6:quit}
        # Select function from menu:
        def get_sel():
            return int(input("\nSelecciona una opcion: "))
        sel = get_sel()
        while not(1 <= sel <= 2):
            print("Error: Input value must be between 1 and 2.")
            self.display_menu()
            sel = get_sel()
        return from_menu[sel]()

    def qtraslacional(self):
        clear_screen()
        # Welcome:
        @f_decorator
        def name(self):
            return self.tra
        print(name(self))

        # Input
        V = float(input("\nIntroduce volumen del recipiente (Litros): "))
        T = float(input("Introduce la temperatura (K): "))
        def get_molecule():
            return int(input("Introduce si la molecula es monoatomica (1) o diatomica (2): "))

        molecule = get_molecule()
        while not(molecule == 1 or molecule == 2):
            print("Error: Input value must be 1 or 2.")
            molecule = get_molecule()

        # Monoatomic case:
        if molecule == 1:
            print('\n{:*<65}'.format(''))
            print('* {:<61} *'.format('Molecula monoatomica'))
            print('{:*<65}\n'.format(''))
            m  = float(input("Introduce la masa (umas): "))

        # Diatomic case:
        elif molecule == 2:
            print('\n{:*<65}'.format(''))
            print('* {:<61} *'.format('Molecula diatomica'))
            print('{:*<65}\n'.format(''))
            m1 = float(input("Introduce la masa del primer atomo (umas): "))
            m2 = float(input("Introduce la masa del segundo atomo (umas): "))
            m = m1 + m2

        # Print data:
        Mm = ((1000. * self.NA)**(-1)) * m       # molecular mass (kg)
        print("\nLa masa de la molecula en kg es: {0}".format(Mm))

        lbdT = self.h / ((2 * math.pi * self.k * T * Mm)**0.5)    # termical wave length
        print("La longitud de onda termica en metros es: {0}".format(lbdT))

        qt =  V * ((lbdT)**(-3))        # traslational partition function
        print("Funcion de particion traslacional: {0}".format(qt))

        print('\n{:*<65}'.format(''))

        system_pause()
        return self.main_screen()

    def qvibracional(self):
        clear_screen()
        # Welcome:
        @f_decorator
        def name(self):
            return self.vib
        print(name(self))

        # Input:
        T = float(input("\nIntroduce la temperatura (K): "))
        def get_vib():
            return int(input("Indique el numero de modos vibracionales en la molecula (1-4): "))

        MN = get_vib()
        while not(1 <= MN <=  4):
            print("Error: Input value must be between 1 and 4.")
            MN = get_vib()

        # Compute data:
        print('\n{:*<65}'.format(''))
        print('* {:^61} *'.format('Modos vibracionales: {}'.format(MN)))
        print('{:*<65}\n'.format(''))

        v = [0]*MN
        Tv = [0]*MN
        qv = 1
        for i in range(MN):
            v[i] = float(input("Introduce modo vibracional {0} (cm-1): ".format(i+1)))
            Tv[i] = (self.h * self.c * v[i]) / (self.k * T)
            qv *= 1 / (1 - math.exp(-Tv[i]))

        print("\nFuncion de particion vibracional: {}".format(qv))
        print('\n{:*<65}'.format(''))

        system_pause()
        return self.main_screen()


if __name__ == "__main__":
    QPART()
