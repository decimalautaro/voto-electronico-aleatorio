class Voto:
  def __init__(self, candidato, esBlanco, esImpugnado,esValido):
    self.candidato = candidato
    self.esBlanco = esBlanco
    self.esImpugnado =esImpugnado
    self.esValido = esValido

  def __str__(self):
      return str("\nCandidato: {} \n" "Es blanco: {} ---" "   Es impugnado: {} ---" "   Es Valido: {}".format(
         self.candidato, 
         self.esBlanco, 
         self.esImpugnado ,
         self.esValido ,
         )
      )

