"""Modulos estandar para ejecucion de programa de calculos estadisticos"""
import sys
import time

def read_data(file_name, data):
    """Funcion para leer datos dentro de archivo .txt"""

    while 1:
        try:
            with open(file_name,encoding="utf-8") as file:
                #Lee los datos y deteta entradas invalidas
                for number in file.readlines():
                    #Si el dato es valido lo agrega
                    try:
                        num = float(number)
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
        if char.isdigit() or char == '.' or char == '-':
            corrected_value += char
        elif char != '\n':
            corrected_value += '.'
    try:
        num = float(corrected_value)
        print("Corrected: " + str(num) + "\n")
        data.append(num)
    except ValueError:
        print("Not possible to correct\n")

def data_mean(data):
    """Funcion para media"""

    x = 0

    #Calculo de media
    for num in data:
        if num is not None:
            x += num
    x = x / len(data)
    return x

def data_median(data):
    """Funcion para mediana"""

    med = 0

    #Caso de cantidad de datos par
    if len(data) % 2 == 0:
        med = (data[len(data) // 2] + data[(len(data) // 2) - 1])/2
    #Caso de cantidad de datos impar
    else:
        med = data[(len(data) // 2)]

    return med

def data_mode(data):
    """Funcion para moda"""

    unrepeated = []
    occur = []

    #Se itera sobre para obtener las repeticiones de los datos
    for num in data:
        if num not in unrepeated:
            unrepeated.append(num)
            occur.append(1)
        else: occur[unrepeated.index(num)] += 1

    counter = 0
    for x in occur:
        if max(occur) == x:
            counter += 1

    if counter > 1:
        mode = "N/A EXISTE MAS DE UNA MODA"
    else:
        mode = unrepeated[occur.index(max(occur))]

    return mode

def data_dev_var(data,mean):
    """Funcion para desviacion estandar"""

    x = 0

    #Calculo de varianza
    for num in data:
        x += (num - mean) ** 2

    #Se retorna desvacion estandar, varianza
    return (x / len(data)) ** 0.5, x / len(data)

def print_results(total,file,statistic_data,exec_time):
    """Funcion para imprimir y guardar datos"""

    #Se crea archivo con resultados
    with open("StatisticsResults_"+file,"w",encoding="utf-8") as file:

        #Total de datos#Impresion de mean
        print("Total: " + str(total))
        file.write("Total: " + str(total) + "\n")

        #Impresion de mean
        print("Mean: " + str(statistic_data[0]))
        file.write("Mean: " + str(statistic_data[0]) + "\n")

        #Impresion de median
        print("Median: " + str(statistic_data[1]))
        file.write("Median: " + str(statistic_data[1]) + "\n")

        #Impresion de mode
        print("Mode: " + str(statistic_data[2]))
        file.write("Mode: " + str(statistic_data[2]) + "\n")

        #Impresion de Standard deviation
        print("Standard Deviation: " + str(statistic_data[3]))
        file.write("Standard Deviation: " + str(statistic_data[3]) + "\n")

        ##Impresion de variance
        print("Variance: " + str(statistic_data[4]))
        file.write("Variance: " + str(statistic_data[4]) + "\n")

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

    #Caldulo de datos estadisticos
    total = len(data)
    mean = data_mean(data)
    median = data_median(sorted(data))
    mode = data_mode(data)
    std_dev,var = data_dev_var(data,mean)

    #Fin de tiempo de ejecucion
    final_time = time.time()

    #Se imprimen y guardan resultados
    print_results(total,file_name,[mean,median,mode,std_dev,var],final_time - init_time)

#Llama a la funcion main()
if __name__ == "__main__":
    #Lee el argumento que es el nombre del archivo
    ARGS = str(sys.argv[1])

    #Invoca a funcion main
    main(ARGS) # End-of-file (EOF)
