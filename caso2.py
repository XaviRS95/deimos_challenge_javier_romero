import caso1

def getJSON():
    csv_data = caso1.readCsv()
    json_data = []
    for row in csv_data[1:]:
        aux_json = {
            'Matricula': row[0],
            'Latitud': float(row[1]),
            'Longitud': float(row[2]),
            'Distance': float(row[3]),
            'Pos_date' : row[4]
        }
        json_data.append(aux_json)
    return json_data

if __name__ == '__main__':
    csv_data = caso1.readCsv()
    columns = csv_data[0]
    for row in csv_data[1:]:
        aux_json = {
            'Matricula': row[0],
            'Latitud': float(row[1]),
            'Longitud': float(row[2]),
            'Distance': float(row[3]),
            'Pos_date': row[4]
        }
        print(aux_json)