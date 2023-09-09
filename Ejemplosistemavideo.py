# Crearemos una función para determinár la clase Ejemplosistemadevideo.

# Traemos las clases "video" y "sistema video".
from Video import Video
from Sistemavideo import Sistemavideo


# Generamos un objeto de la clase SistemaVideo.
sistema = Sistemavideo()

# Incluimos los videos en el catálogo.
sistema.agregarVideo(Video("Perros de Reserva", "D"))
sistema.agregarVideo(Video("Star Wars Episodio III: La Venganza de los Sith", "A"))
sistema.agregarVideo(Video("El Señor de los Anillos II: Las Dos Torres", "B"))
sistema.agregarVideo(Video("Eterno resplandor de una mente sin recuerdos", "C"))


# Asignamos las puntuaciones a los videos.
video1 = sistema.buscarvideoportitulo("Perros de Reserva")
video1.recibirpuntaje(6.9)
video1.recibirpuntaje(7.3)

video2 = sistema.buscarvideoportitulo("Star Wars Episodio III: La Venganza de los Sith")
video2.recibirpuntaje(9.8)
video2.recibirpuntaje(8.8)

video3 = sistema.buscarvideoportitulo("El Señor de los Anillos II: Las Dos Torres")
video3.recibirpuntaje(10)
video3.recibirpuntaje(9.2)

video4 = sistema.buscarvideoportitulo("Eterno resplandor de una mente sin recuerdos")
video4.recibirpuntaje(7.5)
video4.recibirpuntaje(7.8)
video4.recibirpuntaje(6.8)
video4.recibirpuntaje(8.9)

# Ocasiones en las que se alquilarón los videos.
video1.rentar()
video1.rentar()
video2.rentar()
video2.rentar()
video3.rentar()
video3.rentar()
video4.rentar()
video4.rentar()
video4.rentar()
video4.rentar()

# Exhibimos el inventario una vez que "El señor de los Anillos II" ha sido alquilado.
print("Inventario de Videos después de rentar 'El Señor de los Anillos II: Las Dos Torres':")
sistema.mostrarinventario()
