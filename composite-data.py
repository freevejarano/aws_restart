import csv # Modulo es para tratar con archivos csv (comma separated values)
import copy # Modulo para sacar una copia de cierta colección

# Diccionario que cumple como plantilla

myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

# Una forma en que con un solo for se puede imprimir las llaves y sus valores
"""
for key, value in myVehicle.items():
    print("{} : {}".format(key,value))
"""

myInventoryList = [] # Declarando una lista

# MANEJO DE ARCHIVOS, csv

# with open (incluir la ruta / nombre del archivo)
# por defecto tiene un modo de lectura (r)
# modos de lectura (r), escritura (w) y edición (a) (append)

with open("car-fleet.csv") as csvFile:
    csvReader = csv.reader(csvFile) # Archivo se entienda como csv, por defecto el delimiter es ,
    lineCount = 0
    
    for row in csvReader: # Separar el archivo en listas por fila
        # Omitir el nombre de las columnas / encabezado
        if lineCount == 0:
            # .join() es de str para convertir la lista en string
            # Entre comillas se coloca el separador que se quiere
            print(f"El nombre de las columnas son: {', '.join(row)}")
            lineCount += 1
        else:
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')
        
            currentVehicle = copy.deepcopy(myVehicle) # Una copia exacta desvinculada del diccionario original
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]
            
            myInventoryList.append(currentVehicle) # Agrega el vehículo actual a la lista de inventario
            
            lineCount += 1 # Saber cuantas filas hemos tratado
    
    print(f"Se contaron {lineCount} lineas")
    
    print()
    
    # Forma de imprimir los elementos de la lista con su valores ordenados
    # for anidado
    
    for properties in myInventoryList:
        for key, value in properties.items():
            print(f"{key} : {value}")
            print("-"*40)
        print()    