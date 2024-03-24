"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():

    #   
    # Inserte su código aquí
    #
    data = []

    # Ruta al archivo
    file_path = 'clusters_report.txt'

    # Leer el archivo línea por línea
    with open(file_path, 'r') as file:
        # Saltar las primeras dos líneas
        next(file)
        next(file)
        #lines = file.readlines()
        # Iterar sobre las líneas restantes
        #for line in lines[2:]:
        for line in file:
            # Dividir la línea en columnas usando el espacio como delimitador
            columns = line.split()
            if len(columns) >= 1:
                try:
                    first_element =int(columns[0]) 
                    # Extraer los valores de cada columna
                    cluster = first_element
                    cantidad_palabras_clave = int(columns[1])
                    porcentaje_palabras_clave = columns[2]
                    palabras_clave = ' '.join(columns[4:])
                
                    # Agregar los valores de la fila a la lista de datos
                    data.append([cluster, cantidad_palabras_clave, porcentaje_palabras_clave, palabras_clave])
                except:
                    if len(data)>0:
                        #print(columns[0:])
                        STR = ' '.join(columns[0:])
                        data[len(data)-1][3] += " "
                        data[len(data)-1][3] += STR
            

    df = pd.DataFrame(data, columns=['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'])
    df['porcentaje_de_palabras_clave'] = df['porcentaje_de_palabras_clave'].str.replace(',', '.').astype(float)
    df['principales_palabras_clave'] = df['principales_palabras_clave'].str.replace('.', '')
    # Reemplazar espacios en los nombres de las columnas con guiones bajos y convertir a minúsculas
    df.columns = df.columns.str.replace(' ', '_').str.lower()
    #print(df)
    return df

#print(ingest_data().principales_palabras_clave.to_list()[1])
#print(ingest_data())
#print("maximum power point tracking, fuzzy-logic based control, photo voltaic (pv), photo-voltaic system, differential evolution algorithm, evolutionary algorithm, double-fed induction generator (dfig), ant colony optimisation, photo voltaic array, firefly algorithm, partial shade")
