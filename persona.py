
class Persona:

  def __init__(self, nombre, apellido, dni, anioNac, direccion):
    self.nombre = nombre
    self.apellido = apellido
    self.dni = dni
    self.anioNac = anioNac
    self.direccion = direccion 
    

  def __str__(self):
      return ("Nombre: {}" "Apellido: {}" "Dni: {}" "Fecha de Nacimiento: {}" "Calle: {}" "Numero: {} " "Barrio: {}" "Distrito: {}".format(
         self.nombre, 
         self.apellido, 
         self.dni ,
         self.anioNac,
         self.direccion.calle,
         self.direccion.numero,
         self.direccion.barrio,
         self.direccion.distrito,


         )
      )