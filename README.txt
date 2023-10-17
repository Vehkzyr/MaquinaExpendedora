INSTRUCCIONES PARA EJECUTAR EL CÓDIGO DEL AUTÓMATA

1. Preparar el entorno: Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo y encontrar instrucciones de instalación en https://www.python.org/.

2. Ejecutar el script: Abre un terminal o línea de comandos. Navega hasta el directorio que contiene el script y el archivo 'archivo.txt'. Ejecuta el comando: python3 ejecutable.py

3. Usar el programa: Una vez que el script esté en ejecución, se te pedirá que introduzcas una cadena de entrada. Introduce la cadena de entrada que desees que el autómata procese. El programa ejecutará el autómata basado en la cadena proporcionada y mostrará los estados finales alcanzados.

El output del programa deberá ser algo parecido a esto: 

Introduzca la cadena de entrada: 152ac22bd1c2c

Caracter introducido: 1
    Estado(s) Actual(es): ['q00']
    Estado(s) Siguiente(s): ['q10']

Caracter introducido: 5
    Estado(s) Actual(es): ['q10']
    Estado(s) Siguiente(s): ['q15']

Caracter introducido: 2
    Estado(s) Actual(es): ['q15']
    Estado(s) Siguiente(s): ['q35']

Caracter introducido: a
    Estado(s) Actual(es): ['q35']
    Estado(s) Siguiente(s): ['q30', 'qaa']
    Devolviendo ['qaa']

Caracter introducido: c
    Estado(s) Actual(es): ['q30']
    Estado(s) Siguiente(s): ['q10', 'qcc']
    Devolviendo ['qcc']

Caracter introducido: 2
    Estado(s) Actual(es): ['q10']
    Estado(s) Siguiente(s): ['q30']

Caracter introducido: 2
    Estado(s) Actual(es): ['q30']
    Estado(s) Siguiente(s): ['q30']

Caracter introducido: b
    Estado(s) Actual(es): ['q30']
    Estado(s) Siguiente(s): ['q20', 'qbb']
    Devolviendo ['qbb']

Caracter introducido: d
    Estado(s) Actual(es): ['q20']
    Estado(s) Siguiente(s): ['q00', 'qdd']
    Devolviendo ['qdd']

Caracter introducido: 1
    Estado(s) Actual(es): ['q00']
    Estado(s) Siguiente(s): ['q10']

Caracter introducido: c
    Estado(s) Actual(es): ['q10']
    Estado(s) Siguiente(s): ['q10']

Caracter introducido: 2
    Estado(s) Actual(es): ['q10']
    Estado(s) Siguiente(s): ['q30']

Caracter introducido: c
    Estado(s) Actual(es): ['q30']
    Estado(s) Siguiente(s): ['q10', 'qcc']
    Devolviendo ['qcc']



Nota: Este script está diseñado para autómatas definidos específicamente con la estructura esperada en 'archivo.txt'. Asegúrate de que tu autómata esté definido correctamente según los requisitos del script.
