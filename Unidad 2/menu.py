# ALTA PLANTILLA PARA LA CLASE MENU MAMAWEVO

class Menu:
    def __init__(self):
        self.opcion = 0

    def mostrar_menu(self):
        print("1. Opción 1")
        print("2. Opción 2")
        print("3. Opción 3")
        print("4. Salir")

    def leer_opcion(self):
        self.opcion = int(input("Seleccione una opción: "))

    def ejecutar_opcion(self):
        if self.opcion == 1:
            print("Seleccionó la opción 1")
        elif self.opcion == 2:
            print("Seleccionó la opción 2")
        elif self.opcion == 3:
            print("Seleccionó la opción 3")
        elif self.opcion == 4:
            print("Saliendo del programa...")
        else:
            print("Opción no válida")

    def iniciar(self):
        while self.opcion != 4:
            self.mostrar_menu()
            self.leer_opcion()
            self.ejecutar_opcion()
