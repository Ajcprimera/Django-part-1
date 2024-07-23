'''
migraciones: nos ayuda a actualizar nuestro base de datos a 
traves de codigo de python

las migraciones en django nos ayuda de manera mas eficiente a 
crear las tablas con las que vamos a trabajar durante el 
proyecto, para poder hacerlo debemos ejecutar los sgtes 
comandos:

python manage.py makemigrations

python manage.py migrate (ejecuta las migraciones)

y ya nos crea las tablas

no obstante al momento que vayamos a creando nuestra 
aplicacion, quizas veamos la necesidad de crear otras tablas
y para eso lo debemos hacer mediante un modelo

para hacer los modelos hay que ir a nuestra aplicacion y 
desde el archivo models.py crear nuestras tablas para
la aplicacion

nota: para que django conozca nuestros proyectos de nuestra 
aplicacion de debemos realizar la coneccion hacia la carpeta 
del proyecto y para poder hacerlo debemos ir a los settings 
de la rama principal y colocal nuestra aplicacion en enstalled
apps

nota: cuando tablas realacionales lo recomendable que cuando
vayamos a borrar el dato de algunas de las tablas y esta este
unida a otra, bueno lo recomendable que cuando hagamos eso, 
en el modelo coloquemos, on_delete=models.CASCADE y de 
esa manera cuando se elimine el dato tambien se elimine 
todo lo que esta relacionado a el

en settings.py en la parte DATABASE, nos va a ayudar a lo que 
es realizar la coneccion con la base de datos
'''