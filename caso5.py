import caso2
import datetime


def posixToDatetime(posix_timestamp_ms):
    #Transforma POSIX en ms a formato "%d/%m/%Y %H:%M:%S"

    posix_timestamp_sec = posix_timestamp_ms / 1000
    utc_datetime = datetime.datetime.utcfromtimestamp(posix_timestamp_sec)
    formatted_datetime = utc_datetime.strftime("%d/%m/%Y %H:%M:%S")

    return formatted_datetime


if __name__ == '__main__':
    #Obtiene todos los registros de cada matrícula para encontrar cuál es el más reciente de cada uno y lo guarda en un fichero.
    json_data = caso2.getJSON()
    cars_last_date = {}
    for row in json_data:
        if row['Matricula'] not in cars_last_date.keys():
            cars_last_date[row['Matricula']] = row['Pos_date']
        else:
            #Comprobación de fechas posix.
            if (int(cars_last_date[row['Matricula']]) < int(row['Pos_date'])):
                cars_last_date[row['Matricula']] = row['Pos_date']

    with open('caso5_results.txt', 'w') as file:
        for key, value in cars_last_date.items():
            file.write(key + ' (' + posixToDatetime(int(value)) + ')' + '\n')
        file.close()