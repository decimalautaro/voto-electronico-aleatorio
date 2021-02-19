from fecha import Fecha
from votante import Votante
from voto import Voto
from candidato import jorge,roberto,micaela,juan
from random import randint, choice
from direccion import direccionUno,direccionDos,direccionTres,direccionCuatro,direccionCinco,direccionSeis



#genero nombres, apellidos, dni, año de nacimiento, direccion


NOMBRES = ["Lautaro", "Andres", "Luciano", "Alejandro", "Maximiliano", "Franco",
    "Sergio", "Facundo", "Emiliano", "Maria", "Ines", "Sofia", "Agostina",
    "Claudia", "Flavia", "Miriam", "Alicia", "Angelica", "Roxana", "Marcela",
    "Zulma", "Macarena", "Antonella", "Andrea", "Carla"]

APELLIDOS = ["Decima", "Fragaliti", "Jozami", "Conte", "Iglesias", "Gomez", "Sallei",
    "Correa", "Quiroga", "Bustos", "Di Pietro", "Ferreyra", "Coria", "Renna"]

DNI = [randint(20000000, 41999999) for _ in range(500)]

ANIONAC = [
    1968, 1970, 1975, 1978, 1980, 1986, 1988, 1990, 1992, 1994, 1996, 1998,
    2000, 2002
]


DIRECCION = [direccionUno,direccionDos,direccionTres,direccionCuatro,direccionCinco,direccionSeis]


#genero votantes

def generador_votantes (cantidad):
  votantes = []
  for idx in range(cantidad):
    idx_nombres = randint (0,len(NOMBRES)-1)
    idx_apellidos = randint (0,len(APELLIDOS)-1)
    idx_dni = randint (0,len(DNI)-1)
    idx_anioNac = randint (0,len (ANIONAC)-1)
    idx_direccion = randint (0,len(DIRECCION)-1)
   
    voto = generar_voto()
    votante =Votante(NOMBRES [ idx_nombres] , APELLIDOS[ idx_apellidos] ,  DNI [ idx_dni] , ANIONAC [idx_anioNac] , DIRECCION[ idx_direccion] , voto )
    votantes.append (votante)
  return votantes

#FUNNCION PARA GENERAR UN VOTO 
CANDIDATOS= [jorge,roberto,micaela,juan]

def generar_voto():

  tipoVoto = choice([0]*89 + [1]*10 + [2]*1) 
  idx_candidatos = choice ([jorge]*45 + [roberto]*35 + [micaela]*15+ [juan]*5)
 
  voto = Voto(None,False,False,False)
  
  if tipoVoto == 0:
    voto.candidato = idx_candidatos
    voto.esValido = True
  elif tipoVoto == 1: 
    voto.esBlanco = True
  else:
    voto.esImpugnado = True
  return voto


 