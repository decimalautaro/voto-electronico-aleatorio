from persona import Persona
from cargo import Cargo
from lista import Lista
from distrito import Distrito

#CREO EL CONSTRUCTOR DE CANDIDATO
class Candidato(Persona):
  def __init__(self, nombre, apellido, duracion, nombreCargo, numeroLista, partidoPolitico, departamento, provincia):
    Persona.__init__(self, nombre, apellido, dni = None, anioNac = None, direccion= None)
    self.cargo = Cargo (duracion,nombreCargo)
    self.lista = Lista (numeroLista, partidoPolitico)
    self.distrito = Distrito (departamento, provincia)

  def __str__(self):
    return ("\nNombre: {} \nApellido: {} \nCargo: {} \nLista: {} \nPartido Politico: {}\nDistrito: {} \nProvincia {}\n" .format(
      self.nombre, 
      self.apellido, 
      self.cargo.nombreCargo,
      self.lista.numeroLista,
      self.lista.partidoPolitico,
      self.distrito.departamento,
      self.distrito.provincia
    )
  )



#Creo los candidatos.

jorge = Candidato (
 nombre = "Jorge 'Beto'",
 apellido = "López",
 duracion = "4 años" ,
 nombreCargo = "Intendente ",
 numeroLista = 302,
 partidoPolitico = "Cambia Mendoza ",
 departamento = "Lavalle",
 provincia = "Mendoza")

roberto = Candidato (
 nombre = "Roberto",
 apellido = "Righi",
 duracion = "4 años" ,
 nombreCargo = "Intendente ",
 numeroLista = 300,
 partidoPolitico = "Elegí",
 departamento = "Lavalle",
 provincia = "Mendoza")


micaela = Candidato (
 nombre = "Micaela",
 apellido = "Blanco Minoli",
 duracion = "4 años" ,
 nombreCargo = "Intendente ",
 numeroLista = 301,
 partidoPolitico = "Frente de Izquierda",
 departamento = "Lavalle",
 provincia = "Mendoza")


juan = Candidato (
 nombre = "Juan Antonio",
 apellido = "Peña",
 duracion = "4 años" ,
 nombreCargo = "Intendente ",
 numeroLista = 301,
 partidoPolitico = "Frente de Izquierda",
 departamento = "Lavalle",
 provincia = "Mendoza")