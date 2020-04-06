Buscador y Validador de direcciones Gobierno Nacional programado en linux y python3.6

Modo de setup y Uso:

-Descargar el repositorio Desde github, por linea de comando (Linux): wget
-Instalar pip3 para python: sudo apt-get install python3-pip (si no esta instalado)
-Ingresar al directorio, abrir el archivo con un editor de codigo: validador_de_direcciones_nacion.py
-Importar todas las librerias en python (sudo pip3-install <Nombre_de_libreria>)
-Una vez que estan todas las librerias, correr el programa: python3.6 validador_de_direcciones_nacion.py

---------------------------------------------------------------------------------------------------------------

Descripcion y funcionalidades:

Este programa de linea de comando (CLI), es un validador/nomenclador de direcciones de Provincia de Buenos Aires y C.A.B.A.
Permite buscar y validar direcciones en base a 3 campos: 

    -Nombre de calle y Numero separados
    -Localidad o barrio
    -Partido
    
Al proveerle los datos al programa, este consume la API del gobierno nacional:

"https://apis.datos.gob.ar/georef/api/direcciones?provincia="

Si la API encuentra una direccion con los campos suministrados, devolvera los datos Validados en formato .json, los mostrara en la consola y los parseara a formato texto para mostrarlos de manera mas legible para el usuario.




