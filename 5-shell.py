'''
esto nos va a ayudar a de cierta manera a interactuar con la base 
de datos y una manera de hacerlo es mediante el mismo shell
con python manage,py shell y de esa manera podemos de forma 
mas comodad interactuar con la base de datos

nota: importar los modelos para poder trabajar con ellos
ejemplo: from 'nombre_aplicacion'.models import 'Nombre_modelos'
separados por coma

ahora bien una vez estando en la terminal de python para crear
uno dato para la base de datos hacemos lo sgte:

'variable'='nombre_modelo'(name='dato')
para guardar:
'variable'.save()
de esa manera ya guardamos un dato en la base de datos 

ahora bien, existen varias formas de consultar los datos de
nuestra base de datos una forma es la sgte:

todos los datosa traves de una lista:
'nombre_modelo'.objects.all()

dato en especifico:
'nombre_modelo'.objects.get('metodo_dato_a_buscar'='dato')

ahora bien para guardar un dato de una tabla relacional es algo
diferente, primero lo que hacemos es buscar el dato  el cual
queremos relacionar, luego lo guardamos para poder trabajar 
en el:
'variable'= 'nombre_modelo'.objects.get('metodo_dato_a_buscar'='dato')
'variable'.'modelo_relacionado'_set.create(title='dato')

para consultar el dato:
'variable'.'modelo_relacionado'_set.get(id='dato')

para consultar un dato y este retorne una lista vacia o null:
ej: Project.objects,filter(name__startwith='dato')

Nota: el startwith nos permite filtrar por inicio de palabra
'''