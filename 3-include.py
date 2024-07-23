'''
El include nos ayuda a de manera ordenada colocaar nuestras
urls desde nuestra aplicacion hacia la nuestro proyecto 
principal, de esta manera cada aplicacion va a tener sus,
propios urls y para llamarlas lo hacemos mediante el include,
para poder hacerlo primero debemos crear el archivo urls.py 
desde la aplicacion, y desde alli ir colocando todas nuestras 
urls, ademas de importar los modulos para las urls

para poder llamarla lo primero que debemos hacer es importar 
el modulo include (from django.urls import path, include) y 
hacemos lo sgte:
path('', include('nombre_de_la_aplicacion.urls'))

nota: el string vacio que se encuentra antes del include 
significa que antes de las urls no va a ir nada, eso quiere 
decir si al momento que vayamos a visitar la pagina y esta 
no tiene nada significa que se encuentra en la principal y 
sicede de caso contrario que si esta tiene una ruta primero 
debemos colocar la ruta para poder visitarla ya que son 
prefijos
'''