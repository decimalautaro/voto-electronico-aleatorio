from random import randint, choice


class Direccion:
  def __init__(self,calle, numero, barrio, distrito):
    self.numero = calle
    self.calle = numero
    self.barrio = barrio
    self.distrito = distrito

  def __str__(self):
      return str("\nCalle: {} \n" "Numero: {} \n" "Barrio: {} \n" "Distrito: {} \n".format(
         self.numero, 
         self.calle, 
         self.barrio ,
         self.distrito ,
         )
      )




#DIRECCIONES
direccionUno = Direccion(
        calle="Roque Montenegro",
        numero= "S/N",
        barrio="Cipres",
        distrito="Lavalle"),
direccionDos = Direccion(
        calle="Dorrego",
        numero="M 'D' C '1'",
        barrio="Dorrego Sur",
        distrito="Lavalle")

direccionTres = Direccion(
        calle="Ruta N°36",
        numero="M 'A' C '2'", 
        barrio="Los Jarilleros", 
        distrito="Lavalle")

direccionCuatro = Direccion(
        calle="Dorrego y San Carlos", 
        numero="M 'A' C '17'", 
        barrio="Republuca de Peru", 
        distrito="Lavalle")

direccionCinco = Direccion(
        calle="Dorrego", 
        numero=456, 
        barrio="Porvenir", 
        distrito="Lavalle")

direccionSeis = Direccion(calle="Dorrego", 
        numero=909, 
        barrio="Toum", 
        distrito="Lavalle")


