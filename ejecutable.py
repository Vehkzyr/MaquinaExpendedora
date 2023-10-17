
#Definimos la funcion main, la cual sera el tronco del programa
def main():
    #!!!!! SI SE CAMBIA EL NOMBRE DEL ARCHIVO HA DE CAMBIARSE AQUI PARA QUE EL PROGRAMA FUNCIONE !!!!!
    archivo = ('archivo.txt')

    #Llamamos a la funcion cargarAutomata para meter el automata en un diccionario
    automata = cargarAutomata(archivo)
    print(automata)

    entrada = input("Introduzca la cadena de entrada: ")

    estadosFinales = maquinaEstados(entrada, automata)

def cargarAutomata(nombreArchivo):
    """
    Funcion que carga el automata en un diccionario

    :param nombreArchivo - string que almacena el nombre del archivo donde se encuentra el automata
    :return automata - diccionario que almacena la informacion del automata
    """

    # Diccionario para almacenar los componentes del autómata
    automata = {
        "estados": [],
        "estadosFinales": [],
        "simbolos": [], # Se refiere al universo de elementos en el que operara el automata
        "tablaTransiciones": {}
    }

    #Variable auxiliar para contar el numero de iteraciones y saber en que linea estamos
    i = 0

    with open(nombreArchivo, 'r') as file:
        #Leemos el archivo linea por linea
        for linea in file:
            i+=1

            ##################### ESTADOS #####################
            if i == 1:
                #Tenemos en cuenta que por defecto .split utiliza los espacios en blaco como delimitador
                #Metemos en un array los elementos divididos por split
                elementos = linea.split()

                numEstados = elementos[0] #Contiene el numero de elementos del inicio de la linea

                #Metemos los estados en el diccionario con extend, y cogiendo desde el primer elemento hasta el final
                automata["estados"].extend(elementos[1:])

            ################## ESTADOS FINALES #################
            elif i == 2:
                #Realizamos el mismo procedimiento que en el caso anterior

                # Tenemos en cuenta que por defecto .split utiliza los espacios en blaco como delimitador
                # Metemos en un array los elementos divididos por split
                elementos = linea.split()

                numEstadosFinales = elementos[0]  # Contiene el numero de elementos del inicio de la linea

                # Metemos los estados finales en el diccionario con extend, y cogiendo desde el primer elemento hasta el final
                automata["estadosFinales"].extend(elementos[1:])

            ################## SIMBOLOS ########################
            elif i == 3:
                # Realizamos el mismo procedimiento que en el caso anterior

                # Tenemos en cuenta que por defecto .split utiliza los espacios en blaco como delimitador
                # Metemos en un array los elementos divididos por split
                elementos = linea.split()

                numEstadosFinales = elementos[0]  # Contiene el numero de elementos del inicio de la linea

                # Metemos los estados finales en el diccionario con extend, y cogiendo desde el primer elemento hasta el final
                automata["simbolos"].extend(elementos[1:])

                #Añadimos la cadena vacia
                if '' not in automata["simbolos"]:
                    automata["simbolos"].append('')

            ################## TABLA DE TRANSICIONES #################
            elif i >= 5:
                transiciones = [trans.strip() for trans in linea.split("#")[:-1]]  # Elimina '#' y divide la línea en elementos
                estado = automata["estados"][i - 5] #Indicamos que estado es

                # Asumiendo que cada estado tiene un par de símbolo-estado
                automata["tablaTransiciones"][estado] = {}
                # Asigna los estados de transición a los símbolos correspondientes en el diccionario
                for j in range(len(transiciones)):
                    automata["tablaTransiciones"][estado][automata["simbolos"][j]] = transiciones[j]

    return automata

def maquinaEstados (entrada, automata):
    """
    Funcion que a partir de una entrada y un diccionario de datos ejecuta el automata

    :param entrada - string que almacena los inputs del automata que recorrera uno por uno
    :param automata - diccionario que almacena la informacion del automata
    :return estadosFinales - devuelve los estados finales alcanzados por el automata
    """

    ### MANEJO DE LAS TRANSICIONES POR CADENA VACIA (EPSILON) ###
    # Para manejar las transiciones por cadena vacia o epsilon, definiremos la siguiente funcion auxiliar
    def tEpsilon(estados, automata):
        """
        Encuentra todos los estados alcanzables a partir de transiciones epsilon (cadena vacía).

        :param estados - es el conjunto de estados (tambien puede ser solo uno) desde donde exploraremos las transiciones
        :param automata - diccionario de datos que contiene la informacion del automata
        :return alcanzables - devuelve los estados alcanzables por las transiciones
        """
        epsilon = ''  # Cadena vacía representando epsilon

        # Inicialización del conjunto de estados alcanzables con los estados actuales.
        # También asegura que cada estado sea único (sin duplicados).
        alcanzables = estados.copy()

        # Inicialización de la lista de nuevos estados para explorar.
        nuevos = estados.copy()

        # Continúa mientras haya nuevos estados para explorar.
        while nuevos:
            # Los nuevos estados se convierten en los estados actuales
            estadosActuales = nuevos.copy()

            # Limpiamos la variable nuevos para la siguiente iteración
            nuevos.clear()

            for estado in estadosActuales:
                if (epsilon in automata["tablaTransiciones"].get(estado, {})
                        and automata["tablaTransiciones"][estado][epsilon] != ''):

                    # Si hay una transición epsilon obtenemos el estado destino (o los estados)
                    destinos = automata["tablaTransiciones"][estado][epsilon]
                    destinos = destinos.split(' ')
                    for destino in destinos:
                        # Agrega el estado a alcanzables
                        alcanzables.append(destino)
                        # Y lo añadimos también en nuevos para posteriormente iterar sobre él
                        nuevos.append(destino)

        return alcanzables

    # Declaramos el estado(s) actual(es) para saber donde nos encontramos
    estadosActuales = automata["estados"][0]
    estadosActuales = estadosActuales.split(' ')
    estadosActuales = tEpsilon(estadosActuales, automata) #Aplicamos tEpsilon para ver si existe alguna y añadir el estado
    estadosFinales = []  # Almacenamos los estados finales visitados

    # Iteramos a través de cada carácter en el string de entrada
    for caracter in entrada:
        estadosSiguientes = []
        estadosFinalesActuales = [] # variable para imprimir los estados finales actuales

        for estado in estadosActuales:
            # Para evitar el bloqueo del automata, si un estado no tiene una transicion definida en un caracter (es decir
            # que entre un caracter y este definido como '') eliminamos el estado de la lista de estados actuales
            if automata["tablaTransiciones"][estado][caracter] == '':
                estadosActuales.remove(estado)

        for estado in estadosActuales:

            # Buscamos el próximo estado en la tabla de transiciones
            if caracter in automata["tablaTransiciones"][estado] and automata["tablaTransiciones"][estado][caracter] != '':
                # Obtenemos los próximos estados de la tabla de transiciones
                transiciones = automata["tablaTransiciones"][estado][caracter]
                # Puede haber múltiples estados siguientes debido a la naturaleza no determinista del autómata.
                for transicion in transiciones.split(' '):
                    estadosSiguientes.append(transicion)

            else:
                # Si no se encuentra dentro del diccionario sale del bucle
                print(f"ERROR: No hay transición desde {estado} con {caracter}")

        # Aplicamos transiciones epsilon a los estados siguientes para obtener todos los estados alcanzables
        estadosSiguientes = tEpsilon(estadosSiguientes, automata)

        # Comprobamos si alguno de los estados siguientes es un estado final
        esFinal = any(estado in automata['estadosFinales'] for estado in estadosSiguientes)

        if esFinal:
            # Comprobamos si alguno de los estados siguientes es un estado final
            for estado in estadosSiguientes:
                if estado in automata['estadosFinales']:
                    estadosFinales.append(estado)  # Añadimos el estado a la lista solo si es un estado final
                    estadosFinalesActuales.append(estado)

        # Imprimimos los detalles de la transición.
        print(f'\nCaracter introducido: {caracter}')
        print(f'    Estado(s) Actual(es): {estadosActuales}')
        print(f'    Estado(s) Siguiente(s): {estadosSiguientes}')
        if esFinal:
            print(f'    Devolviendo {estadosFinalesActuales}')

        # Actualizamos los estados actuales para la próxima iteración.
        estadosActuales = estadosSiguientes

    return estadosFinales

main()