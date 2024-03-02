import caso2

if __name__ == '__main__':
    #Obtiene los datos en JSON y para cada matrícula, hace el sumatorio de la distancia de cada registro.
    json_data = caso2.getJSON()
    vehicles_distances = {}
    for row in json_data:
        if row['Matricula'] not in vehicles_distances.keys():
            vehicles_distances[row['Matricula']] = row['Distance']
        else:
            vehicles_distances[row['Matricula']] += row['Distance']

    for key, value in vehicles_distances.items():

        print(key, value)