# cura deuda codigos postales

### Pasos para poder correr el repositorio
1.- Se debe crear un ambiente virtual con `python3 -m venv venv` (o solo python en windows)
2.- Una vez instalado el ambiente virtual se activa con el siguiente comando `source venv/bin/activate` o en caso de windows `venv/scripts/activate`
3.- Se clona el repositorio al ambiente de trabajo y se instalan las dependencias con `pip install requirements.txt`. Asegurate de estar en el directorio donde se encuentran los requisitos
4.- Crea un super usuario con el comando `./manage.py createsuperuser` y sigue las instrucciones de creación ( Necesitas el usuario para poder acceder a los endpoints !)
5.- Realiza las migraciones con `./manage.py migrate`
5.- Ahora puedes correr el proyecto con el comando `./manage.py runserver`

Listo! ya puedes acceder a la api. Para hacer peticiones puedes acceder a tu localhost:8000, o directamente desde el proyecto con curl

--Puedes acceder y añadir información a los siguienes recursos: Estados, Municipios, Ciudades, Oficinas Postales y asentamientos( colonias)

Puedes cargar la base de datos a la aplicación con : `./manage.py loaddata data/db.json `. (Este archivo contiene las claves y nombres de los estados)
