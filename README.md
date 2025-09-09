# Portal_Inmobiliario_Hito_3
Hito 3 - Migraciones y recuperación de datos con
Django

Habilidades a evaluar

● Reconocer el significado de una migración y el problema que resuelve para manteneruna adecuada organización de las actualizaciones al esquema de base de datos.
● Utilizar makemigrations para organizar las actualizaciones al esquema de base dedatos.
● Realizar consultas filtradas utilizando el ORM para la recuperación de informaciónacorde al framework Django.
● Ejecutar sentencias de recuperación de datos con SQL con filtros en Django sobre unmotor de base de datos para resolver un problema.
● Ejecutar sentencias CRUD con sentencias SQL sobre un motor de base de datos enDjango para resolver un problema.
Descripción

Una empresa dedicada al arriendo de inmuebles requiere de su ayuda para crear un sitioweb donde usuarios puedan revisar inmuebles disponibles para el arriendo. Por lo tanto, y yahabiendo creado un entorno de trabajo y conectado a nuestra base de datos, debemos continuar en la construcción del proyecto. La siguiente etapa es necesita levantar la información geográfica de Chile (Comunas y Regiones), además necesita generar un script que les permita realizar reportes sobre la aplicación.


Requerimientos

1. Utilizando las migraciones realice lo siguiente:
a. Poblar la base de datos con todas las regiones y comunas de Chile usando loaddata.
b. Poblar de tipos de inmuebles en la base de datos usando loaddata. 
c. Poblar la base de datos con varios inmuebles y usuarios usando loaddata. 

2. Consultar listado de inmuebles para arriendo separado por comunas, solo usando los campos "nombre" y "descripción" en un script python que se conecta a la DB usando DJango y SQL guardando los resultados en un archivo de texto.

3. Consultar listado de inmuebles para arriendo separado por regiones en un script python que se conecta a la DB usando DJango y SQL guardando los resultados en un archivo de texto.