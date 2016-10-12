# PUJScheduler
Interfaz de Python Flask para uso Local para el gestor automático de programación de horarios.


## Recomendaciones

###Para su uso adecuado, se recomienda trabajarlo en sistemas operativos linux
###que adicionalmente posean soporte para el paquete `python-pip` o `pip` para su instalación.

###Dado que esta interfaz funciona de manera local, se recomienda tambien que cualquier dependencia o libreria necesaria para ejecutar el algoritmo sea instalada previamente


## Instalación

###Abriendo la consola de comandos, realizar las siguientes operaciones


1. `sudo apt-get install python-dev build-essential (Solo si hace falta instalar python)` 
2. `sudo apt-get install python-pip`
3. `sudo pip install --upgrade pip`
4. `git clone https://github.com/Mutisantos/PUJScheduler.git`
5. `cd PUJScheduler`
6. `(sudo) pip install requirements` 
7. `python server.py`

### Una vez se ejecuta la ultima linea, poniendo en el navegador localhost:5000 Se puede ver la interfaz ejecutandose 

## Modo de Uso 

Una vez se tiene el servidor en ejecución, la ejecución del algoritmo dependerá 
de las condiciones mencionadas a continuación:

- El algoritmo debe ser capaz de recibir por argumentos de entrada un archivo de texto y generar un archivo de salida 
- Todo algoritmo se ejecutará como si fuera ejecutado en la terminal de comandos, cualquier dependencia debe ser instalada con anterioridad
- Si el algoritmo fue realizado en C o C++, debe introducirse el ejecutable compilado en Linux, usando el comando `g++ -o miAlgoritmo miAlgoritmo.c/cpp/cxx`.
- Si el algoritmo fue realizado en Python, debe introducirse el archivo .py del código
- Si el algoritmo fue realizado en Java, debe introducirse el archivo .class generado al realizar el comando `javac miAlgoritmo.java`.
- Si se planea utilizar otro lenguaje de programación, se solicita avisar con anticipación para darle soporte a la ejecución
- Asegurarse que el archivo a ejecutar tiene permisos de ejecución
- Se recomienda que el algoritmo se encuentre en la misma carpeta que el server.py




