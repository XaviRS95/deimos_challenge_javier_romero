import caso2
import math

def sortByTimestamp(current_registers, new_register):
    #Obtiene los registros asociados a una matrícula y el nuevo registro a incluir,
    #ordenándolos de más recientes a menos.
    def get_timestamp(register):
        #Devuelve el valor de fecha posix en string de un registro.
        return register[2]

    current_registers.append(new_register)
    sorted_registers = sorted(current_registers, key=get_timestamp, reverse=True)
    return sorted_registers


def haversine_distance(coords1, coords2):
    #Calcula la distancia entre 2 coordenadas en formato decinak.

    #Radio de la tierra en kms.
    R = 6371.0

    lat1 = coords1[0]
    lon1 = coords1[1]

    lat2 = coords2[0]
    lon2 = coords2[1]

    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    # Fórmula Haversine que devuelve la distancia en metros.
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c * 1888

    return distance


if __name__ == '__main__':
    json_data = caso2.getJSON()
    #Variable auxiliar para agrupar las coordenadas de cada vehículo ordenadas por fecha poxis de más reciente a menos.
    vehicles_coordinates_timestamps = {}
    for row in json_data:
        if row['Matricula'] not in vehicles_coordinates_timestamps.keys():
            # Inicializar cada colección de registros por cada matrícula incluyendo una lista con las coordenadas y la fecha.
            vehicles_coordinates_timestamps[row['Matricula']] = []
            vehicles_coordinates_timestamps[row['Matricula']].append([row['Latitud'], row['Longitud'], row['Pos_date']])
        else:
            # Si ya hay más de 1 registro, se ordenan por orden de más a menos recientes
            vehicles_coordinates_timestamps[row['Matricula']] = sortByTimestamp(vehicles_coordinates_timestamps[row['Matricula']], [row['Latitud'], row['Longitud'], row['Pos_date']])

    #Se calcula la distancia recorrida total sumando las distancias entre coordenadas con la fórmula Haversine.
    for key, value in vehicles_coordinates_timestamps.items():
        distance = 0
        aux_original_coordinates = (vehicles_coordinates_timestamps[key][0][0], vehicles_coordinates_timestamps[key][0][1])
        for i in range(1, len(vehicles_coordinates_timestamps[key])):
            next_coordinates = (vehicles_coordinates_timestamps[key][i][0], vehicles_coordinates_timestamps[key][i][1])
            distance += haversine_distance(aux_original_coordinates, next_coordinates)
        print(key, distance)