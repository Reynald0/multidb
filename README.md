# Manejar multiples bases de datos con Django #

Antes de empezar, debes tener tus bases de datos creadas (limpias, es decir sin tablas... de preferencia) y poder establecer conexión a cada una de ellas.

**Pasos a seguir:**

## 1. Definir las conexiones a las bases de datos en el **settings.py** de tu proyecto.
[Ver ejemplo](https://github.com/Reynald0/multidb/commit/6b3ba0bd1305eb0ca601cd292927eecbe2a54f3a#diff-5c9fece9bf344c4f8dfa321b50e1e4cc)

## 2. Definir el archivo que routeará la conexión de la aplicación, se recomienda crear un archivo dentro de la aplicación llamado **routers.py**.
Para este ejemplo se usa la aplicación **mi_app_2** y el nombre de la clase es **MiApp2Router**
[Ver ejemplo](https://github.com/Reynald0/multidb/commit/6b3ba0bd1305eb0ca601cd292927eecbe2a54f3a#diff-8a26bbe438600e06c8d7507ebd547ca0)

## 3. Crear una lista llamada **DATABASE_ROUTERS** que contenga la ruta de la clase *dentro de settings.py*.
Para este ejemplo la ruta es **mi_app_2.routers.MiApp2Router**

[Ver ejemplo](https://github.com/Reynald0/multidb/commit/6b3ba0bd1305eb0ca601cd292927eecbe2a54f3a#diff-5c9fece9bf344c4f8dfa321b50e1e4cc)

# ¿Cómo hacer las migraciones? #
Cuando quieras hacer la migración de la aplicación de Django a la base de datos hay que usar el siguiente comando. Sin corchetes, la estructura es la siguiente.

    makemigrations [NOMBRE_APP]
    migrate [NOMBRE_APP] --database [NOMBRE_BASE_DE_DATOS]
    
Donde [NOMBRE_BASE_DE_DATOS] debe ser el nombre de la base de datos que se dió de alta en la variable *DATABASES* del *settings.py*

[Ver ejemplo de la documentación oficial](https://docs.djangoproject.com/en/dev/topics/db/multi-db/#an-example)

[Referencia](https://djangosteps.wordpress.com/2011/11/08/multiple-database-implementation-in-django/)

### Versiones usadas ###
Para este ejemplo se usó:
* Python 3.4.3
* Django 1.11.1
* cymysql
* django-cymysql
