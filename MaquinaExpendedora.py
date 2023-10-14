

#Definimos la funcion main, la cual sera el tornco del programa
def main():
    #!!!!! SI SE CAMBIA EL NOMBRE DEL ARCHIVO HA DE CAMBIARSE AQUI PARA QUE EL PROGRAMA FUNCIONE !!!!!
    archivo = ('archivo.txt')

    #Llamamos a la funcion cargarAutomata para meter el automata en un diccionario
    automata = cargarAutomata(archivo)

    entrada = input("Introduzca la cadena de entrada: ")

    estadosFinales = maquinaEstados(entrada, automata)

    print(f'Productos devueltos: {estadosFinales}')

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

    # Declaramos el estado actual para saber donde nos encontramos
    estadoActual = automata["estados"][0]
    estadosFinales = []  # Almacenar los estados finales visitados

    # Iteramos a través de cada carácter en el string de entrada
    for caracter in entrada:

        # Buscamos el próximo estado en la tabla de transiciones
        if caracter in automata["tablaTransiciones"][estadoActual]:
            # Obtenemos el próximo estado de la tabla de transiciones
            estadoSiguiente = automata["tablaTransiciones"][estadoActual][caracter]
            if(estadoSiguiente == ''):
                estadoSiguiente = estadoActual
        else:
            # Si no se encuentra dentro del diccionario sale del bucle
            print(f"ERROR: No hay transición desde {estadoActual} con {caracter}")
            break

        # Dividimos el estado siguiente en un array auxiliar para mostrar el saldo
        auxSiguiente = [char for char in estadoSiguiente]

        print(f'Caracter introducido: {caracter}, Estado Actual: {estadoActual}, Estado Siguiente: {estadoSiguiente}')
        print(f'    Saldo Actualizado: {auxSiguiente[1]}.{auxSiguiente[2]}')

        #Si el estado siguiente tiene un espacio significa que es doble y contiene un estado final
        #por ejemplo si estamos en el estado q35 y le entra una a transicionamos al estado q30 y nos devuelve qaa 'q30 qaa'
        if ' ' in estadoSiguiente:
            # Dividimos la cadena para obtener los estados individuales
            estados = estadoSiguiente.split(' ')

            # Teniendo en cuenta que el estado final es el segundo tenemos lo siguiente
            estadoNoFinal = estados[0]
            estadoFinal = estados[1]

            # Dividimos el estado siguiente en un array auxiliar para mostrar el producto devuelto
            auxFinal = [char for char in estadoFinal]
            estadosFinales.append(auxFinal[1].upper()) #Con upper convertimos las minusculas en mayusculas para obtener el producto deseado
            print(f"    Devolviendo {auxFinal[1].upper()}")

            # El estado actual se actualiza al estado que no es final
            estadoActual = estadoNoFinal

        else:
            #Si solo hay un estado lo actualizamos
            estadoActual = estadoSiguiente

    return estadosFinales

main()