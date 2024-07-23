'''
para nosotros poder concatenar, ees decir que cuando vayamos 
a una ruta y esta tenga un parametro especial, podemos hacer 
lo sgte, en la zona de las rutas de rutas de urls, cuando 
vayamos a colocar una ruta la cual el mismo usuario quiere 
colocar, solo ponemos <> y dentro el tipo de parametro que este
recibe <str: name>

para concatenarlo hacemos lo sgte:
ej:
return HttpResponse('<h1>Hello %s</h1>' % username)

la concatenacion se hace con %s y luego
'''