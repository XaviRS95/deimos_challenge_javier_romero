from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from mongodb_functionality import mongodb_functionality
app = FastAPI()

#Carga las variables de entorno necesarias conectar con MongoDB
load_dotenv()

#Cargar los datos desde el fichero. Se deja fuera para evitar redundancias de que cada vez que se llama al endpoint
#se tenga que cargar el fichero.
data = {}
with open('caso5_results.txt', 'r') as file:
    for line in file:
        row = line.strip().split(' ')
        data[row[0]] = row[1][1:] + ' ' + row[2][:-1]

#Endpoint del caso 6
@app.get('/get_last_record_date/{carID}')
async def get_last_record_date(carID: str):
    if carID in data.keys():
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                'date': data[carID]
            }
        )
    else:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                None
            }
        )

#Endpoint del caso 8
@app.get('/get_last_record_date_mongo/{carID}')
async def get_last_record_date(carID: str):

    response = mongodb_functionality.getLastDate(carID)

    if response:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                'data': response
            }
        )
    else:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                None
            }
        )
