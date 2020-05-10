# Instalación

> MySQL

1.- Instalar MySQL en Ubuntu.

    sudo apt-get install mysql-server

2.- Entrar a la consola de MySQL

    sudo -i
    mysql

3.- Crear base de datos

    CREATE DATABASE pokepydb CHARACTER SET utf8 COLLATE utf8_general_ci;

4.- Asignar permisos al usuario.

    GRANT ALL PRIVILEGES ON pokepydb.* TO 'pokepyadmin'@'%' IDENTIFIED BY 'pokepy_pass' WITH GRANT OPTION;
    
    FLUSH PRIVILEGES;

> CELERY

Estas son las variables que deben ir en el settings

    https://django.readthedocs.io/en/latest/topics/settings.html#envvar-DJANGO_SETTINGS_MODULE
    https://docs.celeryproject.org/en/latest/userguide/configuration.html#configuration

El como integrar Celery en Django se obtuvo de aqui:

    https://docs.celeryproject.org/en/latest/django/first-steps-with-django.html#using-celery-with-django

