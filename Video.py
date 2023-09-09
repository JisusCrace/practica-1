print("\n")
print("***************")
print("Práctica 1")
print("***************")

"""
Autor: Ramirez Aguilera Jesús Emmanuel. 
Matricula: 2223068873

Objetivo: Desarrollar un servicio de streaming que sea modular, bien estructurado y se adhiera a 
los fundamentos de la programación orientada a objetos.

Problematica:  
Un servicio de renta de videos por streaming requiere un sistema básico de registro y calificación de videos.
  
"""
# Iniciamos con la definición de la clase de video.
class Video:
    def __init__(self, titulo, clasificacion):
        self.titulo = titulo
        self.clasificacion = clasificacion
        self.vecesrentado = 0
        self.puntajeObtenido = 0
        self.puntajePromedio = 0.0

    def gettitulo(self):
        return self.titulo

    def getclasificacion(self):
        return self.clasificacion

    def rentar(self):
        self.vecesrentado += 1

    def getvecesrentado(self):
        return self.vecesrentado

    def puntajePromedio(self):
        return self.puntajePromedio

    def recibirpuntaje(self, puntaje):
        self.puntajeObtenido += 1
        self.puntajePromedio = ((self.puntajePromedio * (self.puntajeObtenido - 1)) + puntaje) / self.puntajeObtenido

# Se muestran las propiedades.
    def __str__(self):
        return "\nTitulo: " + self.titulo + "\nClasificacion: " + self.clasificacion + "\nVeces rentado: " + str(
            self.vecesrentado) + "\nPuntaje Promedio: " + str(self.puntajePromedio)
