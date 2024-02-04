"""Modulos estandar para ejecucion de programa de conversion de binario y hexadecimal"""
import sys
import time

def read_data(file_name, data):
    """Funcion para leer datos dentro de archivo .txt"""

    while 1:
        try:
            with open(file_name,encoding="utf-8") as file:
                #Lee los datos y detecta entradas invalidas
                for number in file.readlines():
                    #Si el dato es valido lo agrega
                    try:
                        num = int(number)
                        data.append(num)
                    except ValueError:
                        correct_data(data,number)
            break
        except EnvironmentError:
            print("File not found\nFile name: ")
            file_name = input()

def correct_data(data,value):
    """Funcion para manejar datos incorrectos"""

    print("Invalid data:  " + value)
    corrected_value = ""

    #Ciclo para detectar letras/simbolos
    for char in value:
        if char.isdigit() or char == '-':
            corrected_value += char
    try:
        num = int(corrected_value)
        print("Corrected: " + str(num) + "\n")
        data.append(num)
    except ValueError:
        print("Not possible to correct\n")

def to_binary(data):
    """Funcion para convertir de decimal a binario"""

    binary_data = []

    #Iterar sobre la lista
    for number in  data:
        b_num = ""

        #Caso 0
        if number == 0:
            binary_data.append("0")

        #Caso numero positivo
        elif number > 0:
            while number > 0:
                b_num += str(number % 2)
                number //= 2
            b_num = b_num[::-1]
            binary_data.append(b_num)

        #Caso numero negativo
        else:
            number = (-number - 1) ^ 0xFFFFF
            while number > 0:
                b_num += str(number % 2)
                number //= 2
            b_num = b_num[::-1]
            binary_data.append(b_num)

    return binary_data

def to_hex(data):
    """Funcion para convertir de decimal a hexadecimal"""

    #Tabla para tomar valor de hexadecimal
    hex_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A',
                11: 'B', 12: 'C',13: 'D', 14: 'E', 15: 'F'}
    hex_data = []

    #Iterar sobre los datos
    for number in  data:
        hex_num = ""

        #Caso 0
        if number == 0:
            hex_data.append("0")

        #Caso numero positivo
        elif number < 0:
            number = -number - 1 ^ 0xFFFFFFFFFFFFFFFF
            while number > 0:
                hex_num += hex_table[number % 16]
                number //= 16
            hex_num = hex_num[::-1]
            hex_data.append(hex_num)

        #Caso numero negativo
        else:
            while number != 0:
                hex_num += hex_table[number % 16]
                number //= 16
            hex_num = hex_num[::-1]
            hex_data.append(hex_num)

    return hex_data

def print_results(name,data,b_data,h_data,exec_time):
    """Funcion para imprimir y guardar datos"""

    #Se crea archivo con resultados
    with open("ConvsersionResults_"+name,"w",encoding="utf-8") as file:

        #Encabezado
        print("Decimal\t\tBinary\t\tHexadecimal")
        file.write("Decimal\t\tBinary\t\tHexadecimal\n")

        #Impresion de datos binarios y hexa
        for x in range(0,len(data),1):
            print(str(data[x]) + "\t\t" + b_data[x] + "\t\t" + h_data[x])
            file.write(str(data[x]) + "\t\t" + b_data[x] + "\t\t" + h_data[x] + '\n')

        #Impresion de tiempo
        print("\nExecution time: " + str(exec_time))
        file.write("\nExecution time: " + str(exec_time))

def main(file_name):
    """Funcion principal"""

    #Inicio de tiempo de ejecucion
    init_time = time.time()

    #Se leen datos de archivo de texto
    data = []
    read_data(file_name,data)

    binary = to_binary(data)
    hexa = to_hex(data)

    #Fin de tiempo de ejecucion
    final_time = time.time()

    #Se imprimen y guardan resultados
    t_exec = final_time - init_time
    print_results(file_name,data, binary, hexa, t_exec)

#Llama a la funcion main()
if __name__ == "__main__":
    #Lee el argumento que es el nombre del archivo
    ARGS = str(sys.argv[1])

    #Invoca a funcion main
    main(ARGS) # End-of-file (EOF)
