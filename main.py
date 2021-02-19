from genera import generador_votantes
from candidato import jorge,roberto,micaela,juan



def main ():

  #genero cantidad de votantes 
  cantidadVotantes= 500
  total = generador_votantes(cantidadVotantes)
  
  #inicializo los contadores
  contadorJorge=0
  contadorRoberto=0
  contadorMicaela=0
  contadorJuan=0

  contadorBlancos = 0
  contadorValidos = 0
  contadorImpugnado = 0
  
  
#recorro resultados para poder contar los votos 
  for contador in total:
    print ("Votante: {}".format (contador))
  for i in total:
    if i.voto.esValido == True:
      contadorValidos += 1
    if i.voto.esBlanco == True:
      contadorBlancos  += 1
    if i.voto.esImpugnado == True:
      contadorImpugnado += 1
    if i.voto.candidato == jorge :
        contadorJorge += 1
    if i.voto.candidato == roberto :
        contadorRoberto += 1
    if i.voto.candidato == micaela :
        contadorMicaela += 1
    if i.voto.candidato == juan :
        contadorJuan += 1        

  #paso a porcentaje
  contadorValidos = contadorValidos  * 100 / cantidadVotantes
  contadorBlancos = contadorBlancos * 100 / cantidadVotantes
  contadorImpugnado = contadorImpugnado * 100 / cantidadVotantes
  contadorJorge = contadorJorge * 100/ cantidadVotantes
  contadorRoberto = contadorRoberto * 100/ cantidadVotantes
  contadorMicaela = contadorMicaela * 100/ cantidadVotantes
  contadorJuan = contadorJuan * 100/ cantidadVotantes


  print ("Resultado:\nValidos {}%\n" "Blancos {}%\n" "Impugnados {}%\n" .format (contadorValidos,contadorBlancos,contadorImpugnado ,end = " "))

  print ("Resultado de los candidatos:\n"  
  "*El Candidato Jorge López tiene: {}% \n"
  "*El Candidato Roberto Righi tiene: {}% \n"
  "*El Candidato Micaela Blanco Minoli tiene: {}% \n"
  "*El Candidato Juan Antonio Peña tiene: {}% \n\n".format (contadorJorge, contadorRoberto, contadorMicaela, contadorJuan ))

 

  if  contadorJorge> 40 :
    print ("El ganador es Jorge López con un: "  + str (contadorJorge)+"%" )

  else:
    print ("Hay una segunda vuelta entre:\nJorge López que obtuvo {}% y Roberto Righi que obtuvo el {}% ".format (contadorJorge, contadorRoberto))

if __name__== "__main__":
    main()