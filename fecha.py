class Fecha:

  def __init__(self,anio):

    self.anio = anio

  def __str__(self):
    return "{}".format(     
      self.anio,
    )