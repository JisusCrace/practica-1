#Establecemos la estructura de Sistema de Video

class Sistemavideo:
    def __init__(self):
        self.inventario = []


#Creamos la función para agregár un video.

    def agregarVideo(self, video):
        self. inventario.append(video)


#Creamos la funcion para poder encontrar un video mediante su titulo.

    def buscarvideoportitulo(self, titulo):
        for video in self.inventario:
            if video.gettitulo().lower() == titulo.lower():
                return video


#Creamos la función para eliminar un video.

    def eliminarvideo(self, titulo):
        self.inventario = [video for video in self.inventario if not video.gettitulo().lower() == titulo.lower()]


#Creamos la función para mostar el inventario.

    def mostrarinventario(self):
        for video in self. inventario:
            print(video)


#Creamos la funcion para encontrar un video medienate su titulo.

    def buscarvideoportitulo(self, titulo):
        for video in self.inventario:
            if video.gettitulo().lower() == titulo.lower():
                return video


#Creamos la función por si el video no se encuentra, devuelve "vacío" o "None".
        return None




