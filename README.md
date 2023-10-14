# Maquina Expendedora a Partir de un automata de estados

Este proyecto consiste en la creacion de una maquina de estados para aplicar su funcionamiento a una maquina expendedora la cual tendra tres productos:

| Producto | Precio |
|----------|--------|
| A        | 0,50€  |
| B        | 1,00€  |
| C        | 2,00€  |

Se aceptarán únicamente monedas de 0,50€, 1€ y 2€, hasta un importe máximode 3,50€. La máquina dispone de 4 botones (A, B, C, uno por producto, y D,para devolución del saldo pendiente). La máquina permitirá realizar varias transacciones mientras exista saldo suficiente. El saldo pendiente se devolverá únicamente al pulsar el botón de devolución.

# Funcionalidades

El proyecto incluirá las siguientes funcionalidades:
  - Aceptar las entradas por teclado: simulará la introducción de monedas y
    la pulsación de botones, mediante una cadena de caracteres.
      - Visualizar el comportamiento del autómata paso a paso,
        indicando el/los estado/s en que se encuentra en cada momento
  -  El estado del AF siempre indicará el saldo disponible. Además, en algunos casos el AF podrá estar al mismo tiempo en un estado final que indique el producto que se va a expedir o bien la “acción de devolución”.

# Uso
INSTRUCCIONES PARA EJECUTAR EL CÓDIGO DEL AUTÓMATA

1. Preparar el entorno:
   Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo y encontrar instrucciones de instalación en https://www.python.org/.

2. Preparar el archivo de autómata:
   
  La definición del autómata (alfabeto, conjunto de estados, función de transición, estado inicial y conjunto de estados finales) deberá leerse de un fichero de texto, por lo que habra que pasarle el automata de     la siguiente manera a traves de un txt.

  Formato obligatorio del fichero:
  ```
  #número total de estados estado1 estado2 …
  #número de estados finales estadoFinal1 estadoFinal2 …
  #número total de símbolos del alfabeto simbolo1 simbolo2 … símbolo n
  --TABLA DE TRANSICIONES--
  TANTAS FILAS COMO ESTADOS
  TANTAS COLUMNAS COMO SÍMBOLOS DEL ALFABETO + 1 (cadena vacía).
  Cada columna finaliza con el símbolo #
  ```

  Ejemplo:
  ```
  #4 q00 q10 q20 qaa
  #1 qaa
  #3 1 2 a
  --TABLA DE TRANSICIONES—
  q10 # q20 # # q10 q20 qaa #
  ```

3. Ejecutar el script:
   Abre un terminal o línea de comandos.
   Navega hasta el directorio que contiene el script y el archivo 'archivo.txt'.
   Ejecuta el comando: python MaquinaExpendedora.py.

4. Usar el programa:
   Una vez que el script esté en ejecución, se te pedirá que introduzcas una cadena de entrada.
   Introduce la cadena de entrada que desees que el autómata procese.
   El programa ejecutará el autómata basado en la cadena proporcionada y mostrará los estados finales alcanzados.

   ## Ejemplo de funcionamiento

   Para la cadena de entrada “152ac22bd1c2c”, el funcionamiento del AF será:

   | Entrada |   1   |   5   |   2   |   a   |   c   |   2   |   2   |   b   |   d   |   1   |   c   |   2   |   c   |
   |---------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
   | Estados | {q00} | {q10} | {q15} | {q35} | {q30, qaa} | {q10, qcc} | {q30} | {q30} | {q20, qbb} | {q00, qdd} | {q10} | {q10} | {q30} | {q10, qcc} |

5. Interpretar la salida:
   El programa imprimirá los estados finales alcanzados después de procesar la cadena de entrada a través del autómata.
   Si se encuentra un error, como una transición no definida, el programa imprimirá un mensaje de error correspondiente.

Nota: Este script está diseñado para autómatas definidos específicamente con la estructura esperada en 'archivo.txt'. Asegúrate de que tu autómata esté definido correctamente según los requisitos del script.

# Créditos

Este proyecto fue creado por Pablo Seijo como parte de la asignatura Teoria de Automatas y Lenguajes Formales en la ETSE (USC)
