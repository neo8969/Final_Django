import re

# Función para pedir y validar el ID del usuario, nombre y cantidad de videos
def solicitar_datos_usuario():
    while True:
        id_usuario = input("Por favor, introduce tu número de nómina: ")
        if not re.match("^[A-Za-z0-9]+$", id_usuario):
            print("Nómina en formato incorrecto. Debe capturar solo números y letras.")
            continue

        nombre_usuario = input("Por favor, introduce tu nombre: ")
        if not re.match("^[A-Za-z ]+$", nombre_usuario):
            print("Nombre de usuario en formato incorrecto. Debe capturar solo letras.")
            continue

        try:
            cantidad_videos = int(input("Por favor, introduce la cantidad de videos que subirás: "))
        except ValueError:
            print("Cantidad de videos en formato incorrecto. Debe capturar solo números.")
            continue

        return id_usuario, nombre_usuario, cantidad_videos

# Función para capturar los datos de cada video
def capturar_datos_videos(cantidad_videos):
    videos = []
    for i in range(cantidad_videos):
        print(f"\nDatos del video {i + 1}:")
        while True:
            titulo = input("Introduce el título del video: ")
            if not re.match("^[A-Za-z0-9 ]+$", titulo):
                print("Título del video en formato incorrecto. Debe capturar solo números y letras.")
                continue

            nombre_video = input("Introduce el nombre del video: ")
            if not re.match("^[A-Za-z0-9 ]+$", nombre_video):
                print("Nombre del video en formato incorrecto. Debe capturar solo números y letras.")
                continue

            extension = input("Introduce la extensión del video (.mpg, .mov, etc): ")
            if not re.match("^[A-Za-z0-9.]+$", extension):
                print("Extensión del video en formato incorrecto. Debe capturar solo números y letras.")
                continue

            try:
                tamano = float(input("Introduce el tamaño del video (en megas, no mayor a 3): "))
                if tamano < 0 or tamano > 3:
                    raise ValueError
            except ValueError:
                print("El archivo no debe pesar más de 3 MB.")
                continue

            videos.append((titulo, nombre_video, extension, tamano))
            break

    return videos

# Función para escribir los datos en un archivo
def guardar_datos_archivo(id_usuario, nombre_usuario, videos):
    with open("salida.txt", "w") as archivo:
        archivo.write(f"{id_usuario} | {nombre_usuario} | {len(videos)}")
        for video in videos:
            archivo.write(f" | {' | '.join(str(v) for v in video)}")
    print("\nInformación guardada exitosamente en 'salida.txt'.")

# Programa principal
def main():
    id_usuario, nombre_usuario, cantidad_videos = solicitar_datos_usuario()
    videos = capturar_datos_videos(cantidad_videos)
    guardar_datos_archivo(id_usuario, nombre_usuario, videos)

if __name__ == "__main__":
    main()
