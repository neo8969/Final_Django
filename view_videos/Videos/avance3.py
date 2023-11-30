import re

class Persona:
    def __init__(self):
        self.nombre = ""
        self.id = ""

    def capturar_nombre(self):
        self.nombre = input("Por favor, introduce tu nombre: ")
        if not re.match("^[A-Za-z ]+$", self.nombre):
            print("Nombre de usuario en formato incorrecto. Debe capturar solo letras.")
            return False
        return True

    def capturar_id(self):
        self.id = input("Por favor, introduce tu número de nómina: ")
        if not re.match("^[A-Za-z0-9]+$", self.id):
            print("Nómina en formato incorrecto. Debe capturar solo números y letras.")
            return False
        return True

    def imprimir_nombre(self):
        print(f"Nombre: {self.nombre}")

    def imprimir_id(self):
        print(f"ID (Nómina): {self.id}")

class Videos:
    def __init__(self):
        self.nombre = ""
        self.extension = ""
        self.tamano = 0.0

    def capturar_nombre(self):
        self.nombre = input("Introduce el nombre del video: ")
        if not re.match("^[A-Za-z0-9 ]+$", self.nombre):
            print("Nombre del video en formato incorrecto. Debe capturar solo números y letras.")
            return False
        return True

    def capturar_extension(self):
        self.extension = input("Introduce la extensión del video (.mpg, .mov, etc): ")
        if not re.match("^[A-Za-z0-9.]+$", self.extension):
            print("Extensión del video en formato incorrecto. Debe capturar solo números y letras.")
            return False
        return True

    def capturar_tamano(self):
        try:
            self.tamano = float(input("Introduce el tamaño del video (en megas, no mayor a 3): "))
            if self.tamano < 0 or self.tamano > 3:
                raise ValueError
        except ValueError:
            print("El archivo no debe pesar más de 3 MB.")
            return False
        return True

    def imprimir_nombre(self):
        print(f"Nombre del Video: {self.nombre}")

    def imprimir_extension(self):
        print(f"Extensión del Video: {self.extension}")

    def imprimir_tamano(self):
        print(f"Tamaño del Video: {self.tamano} MB")

# Función para guardar los datos en un archivo
def guardar_datos_archivo(persona, lista_videos):
    with open("salida1.txt", "w") as archivo:
        archivo.write(f"{persona.id} | {persona.nombre} | {len(lista_videos)}")
        for video in lista_videos:
            archivo.write(f" | {video.nombre} | {video.extension} | {video.tamano}")
    print("\nInformación guardada exitosamente en 'salida.txt'.")

# Programa principal
def main():
    persona = Persona()
    while not persona.capturar_id() or not persona.capturar_nombre():
        pass

    lista_videos = []
    try:
        cantidad_videos = int(input("Por favor, introduce la cantidad de videos que subirás: "))
    except ValueError:
        print("Cantidad de videos en formato incorrecto. Debe capturar solo números.")
        return

    for _ in range(cantidad_videos):
        video = Videos()
        while not video.capturar_nombre() or not video.capturar_extension() or not video.capturar_tamano():
            pass
        lista_videos.append(video)

    guardar_datos_archivo(persona, lista_videos)

if __name__ == "__main__":
    main()
