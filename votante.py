from persona import Persona

class Votante(Persona):
  def __init__(self,nombre, apellido, dni, anioNac, direccion, voto):
    Persona.__init__(self, nombre, apellido, dni, anioNac, direccion)
    self.voto = voto 

  def __str__(self):
      return ("\nNombre: {} \n" "Apellido: {} \n" "Dni: {} \n" "Año de nacimiento: {} \n" "Direccion: {} \n" "Votó: {} \n".format(
         self.nombre, 
         self.apellido, 
         self.dni ,
         self.anioNac,
         self.direccion,
         self.voto
         )
      )
