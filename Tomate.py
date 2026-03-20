class Canastilla:
    def __init__(self, cantidad, calidad):
        self.cantidad = cantidad
        self.calidad = calidad

    def __str__(self):
        return f"Canastilla - Cantidad: {self.cantidad} - Calidad: {self.calidad}"


class NodoSimple:
    def __init__(self, canastilla):
        self.canastilla = canastilla
        self.siguiente = None


class ListaSimpleCircular:
    def __init__(self):
        self.cabeza = None

    def agregar(self, canastilla):
        nuevo = NodoSimple(canastilla)

        if not self.cabeza:
            self.cabeza = nuevo
            nuevo.siguiente = self.cabeza
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente

            actual.siguiente = nuevo
            nuevo.siguiente = self.cabeza

    def mostrar(self):
        if not self.cabeza:
            print("Lista vacía")
            return

        actual = self.cabeza
        while True:
            print(actual.canastilla)
            actual = actual.siguiente
            if actual == self.cabeza:
                break


class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None


class ListaDobleCircular:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo = NodoDoble(dato)

        if not self.cabeza:
            self.cabeza = nuevo
            nuevo.siguiente = nuevo
            nuevo.anterior = nuevo
        else:
            ultimo = self.cabeza.anterior

            ultimo.siguiente = nuevo
            nuevo.anterior = ultimo
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo

    def mostrar(self):
        if not self.cabeza:
            print("Lista vacía")
            return

        actual = self.cabeza
        while True:
            print(actual.dato)
            actual = actual.siguiente
            if actual == self.cabeza:
                break


class Helado:
    def __init__(self, id, cantidad, precio):
        self.id = id
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"Helado {self.id} - Cantidad: {self.cantidad} - Precio: ${self.precio}"


class SistemaTomate:
    def __init__(self):
        self.recoleccion = ListaSimpleCircular()
        self.produccion = ListaDobleCircular()
        self.ventas = ListaDobleCircular()
        self.contador_helados = 1

    def recolectar(self):
        try:
            cantidad = int(input("Cantidad de tomates en la canastilla: "))
            calidad = input("Calidad (primera/segunda): ").lower().strip()

            if calidad not in ["primera", "segunda"]:
                print("Calidad inválida\n")
                return

            canastilla = Canastilla(cantidad, calidad)
            self.recoleccion.agregar(canastilla)
            print("Canastilla agregada\n")

        except:
            print("Error en los datos\n")

    def seleccionar(self):
        if not self.recoleccion.cabeza:
            print("No hay canastillas\n")
            return

        self.produccion = ListaDobleCircular()

        actual = self.recoleccion.cabeza

        while True:
            if actual.canastilla.calidad == "primera":
                self.produccion.agregar(actual.canastilla)

            actual = actual.siguiente
            if actual == self.recoleccion.cabeza:
                break

        print("Selección completada\n")

    def producir_helados(self):
        if not self.produccion.cabeza:
            print("No hay canastillas de primera\n")
            return

        try:
            precio = float(input("Precio del helado: "))
        except:
            print("Precio inválido\n")
            return

        actual = self.produccion.cabeza

        while True:
            cantidad_helados = actual.dato.cantidad

            helado = Helado(self.contador_helados, cantidad_helados, precio)
            self.ventas.agregar(helado)

            self.contador_helados += 1

            actual = actual.siguiente
            if actual == self.produccion.cabeza:
                break

        print("Helados producidos\n")

    def mostrar_recoleccion(self):
        print("\n--- RECOLECCIÓN ---")
        self.recoleccion.mostrar()

    def mostrar_produccion(self):
        print("\n--- CANASTILLAS DE PRIMERA ---")
        self.produccion.mostrar()

    def mostrar_ventas(self):
        print("\n--- HELADOS ---")
        self.ventas.mostrar()


def menu():
    sistema = SistemaTomate()

    while True:
        print("\n1. Recolectar canastilla")
        print("2. Mostrar recolección")
        print("3. Seleccionar canastillas de primera")
        print("4. Mostrar producción")
        print("5. Producir helados")
        print("6. Mostrar ventas")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            sistema.recolectar()
        elif opcion == "2":
            sistema.mostrar_recoleccion()
        elif opcion == "3":
            sistema.seleccionar()
        elif opcion == "4":
            sistema.mostrar_produccion()
        elif opcion == "5":
            sistema.producir_helados()
        elif opcion == "6":
            sistema.mostrar_ventas()
        elif opcion == "7":
            print("Saliendo...")
            break
        else:
            print("Opción inválida")


menu()