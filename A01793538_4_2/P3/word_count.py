"""Modulos estandar para ejecucion de programa de conversion de binario y hexadecimal"""
import sys
import time

def read_data(file_name):
    """Funcion para leer datos dentro de archivo .txt"""

    while 1:
        try:
            with open(file_name,encoding="utf-8") as file:
                #Lee los datos y detecta entradas invalidas
                try:
                    text = file.read()
                    return clear_data(text)
                except ValueError:
                    print("Error in data, try other file: ")
                    file_name = input()
                    continue
            break
        except EnvironmentError:
            print("File not found\nFile name: ")
            file_name = input()

def clear_data(text):
    """Funcion para encontrar palabras repetidas"""

    clean_data = []
    for word in text.split('\n'):
        clean_data.append(word)

    return clean_data

def word_repeat(data):
    """Funcion para encontrar palabras repetidas"""

    unrepeated = []
    occur = []

    #Se itera sobre para obtener las repeticiones de los datos
    for word in data:
        if word not in unrepeated:
            unrepeated.append(word)
            occur.append(1)
        else: occur[unrepeated.index(word)] += 1

    return unrepeated,occur

def print_results(name,words,repeat,exec_time):
    """Funcion para imprimir y guardar datos"""

    #Se crea archivo con resultados
    with open("WordCountResults_"+name,"w",encoding="utf-8") as file:

        #Encabezado
        print("Word\t\tRepeat")
        file.write("Word\t\tRepeat\n")

        #Impresion de datos binarios y hexa
        for x in range(0,len(words),1):
            print(words[x] + "\t\t" + str(repeat[x]))
            file.write(words[x] + "\t\t" + str(repeat[x]) + "\n")

        #Impresion de tiempo
        print("\nExecution time: " + str(exec_time))
        file.write("\nExecution time: " + str(exec_time))

def main(file_name):
    """Funcion principal"""

    #Inicio de tiempo de ejecucion
    init_time = time.time()

    #Se leen datos de archivo de texto
    data = read_data(file_name)

    words, repeat = word_repeat(data)

    #Fin de tiempo de ejecucion
    final_time = time.time()

    #Se imprimen y guardan resultados
    t_exec = final_time - init_time
    print_results(file_name,words,repeat,t_exec)

#Llama a la funcion main()
if __name__ == "__main__":
    #Lee el argumento que es el nombre del archivo
    ARGS = str(sys.argv[1])

    #Invoca a funcion main
    main(ARGS) # End-of-file (EOF)