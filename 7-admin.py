'''
Django tiene un panel llamado panel de superusuario, el  cual 
nos permite controlar o administrar la aplicacion, no obstante 
para acceder a ella debemos primero crear el usuario y eso se 
hace mediante el sgte comando:

python manage.py createsuperuser

ahora bien, si queremos que desde ese mismo panel administrar 
los modelos de la aplicacion la cual estamos trabajando debemos 
hacerlo desde el archivo admins de nuestra aplicacion de la sgte 
manera:

admin.site.register("nombre_modelo")
'''