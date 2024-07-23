'''
Para crear nuestro primer proyecto debemos irnos a la terminal
y ejecutar el sgte comando

django-admin startproject 'nombre_proyecto'
nota: es recomendable no colocarle nombres como django, python 
o test ya que tendriamos complicaciones con las librerias

Ahora bien si queremos que el proyecto no este una carpeta 
dentro de otra, podemos ejecutar el sgte comando

django-admin startproject 'nombre_proyecto' .

al ejecutar estos comandos este genera una carpeta la cual nos 
permite crear codigo para nuestro proyecto y un archivo para 
administrarlo

el archivo nos ayuda ejecutar los comandos para nuestro proyecto 
como ejecutar un servidor de desarrollo

comando para ejecutar el servidor de nuestro proyecto:
python manage.py runserver

comando para cambiar puerto del servidor:
python manage.py runserver 3000

comando para iniciar una aplicacion para el servidor:
python manage.py startapp 'nombre_aplicacion'
nota: para llamar estas aplicaiones debemos hacerlo desde la 
carpeta principal o proyecto principal ya que es el nucleo de 
la app y no permite crear todas las configuraciones
'''