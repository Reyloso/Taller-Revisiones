# Taller-Revisiones

App realizada en el framework Django como ejemplo de un CRUD para La clase de bases de datos

#Proyecto Ejmeplo para el curso de base de datos

#Instalacion en su equipo

Requerimientos

Python/Django(paquete bitnami django en windows)

PostgreSQL

Instalación

Crear un virtualenv(entorno virtual)

Instalar dependencias

$ pip install -r requirements.txt


II. Base de datos

Todas las configuraciones para trabajar con una base de datos en en el proyecto utilizando PostgreSQL.

Conexión a la base de datos

En el archivo $ biblioteca/settings.py

 DATABASES = {
        'default': {
            'ENGINE':                    'django.db.backends.postgresql_psycopg2',
            'NAME': '$nombre_db',
            'USER': '$nombre_usuario',
            'PASSWORD': '$contraseña,
            'HOST': 'localhost',
            'PORT': '',
        }
}
