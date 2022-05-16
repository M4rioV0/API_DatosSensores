from re import sub
from django.core.management.base import BaseCommand
import json
from datetime import datetime
from DatosSensores.models import Avg8Hours

data = open("C://Users\mario\dev\API\API_prueba\data\AvgDiary.json","r")

x = data.read()

data.close()

json_ = json.loads(x)

class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        for linea in json_:

            avgCO = linea["avgCO"]
            avgNo2 = linea["avgNo2"]
            avgO3 = linea["avgO3"]
            avgPm1 = linea["avgPm1"]
            avgPm10 = linea["avgPm10"]
            avgPm2_5 = linea["avgPm2_5"]
            dateIni = linea["dateIni"]
            idStation = linea["idStation"]
            timestamp = linea["timestamp"]
            
            dateIni = dateIni/1000
            timestamp = timestamp/1000

            di = datetime.fromtimestamp(dateIni)
            tt = datetime.fromtimestamp(timestamp)

            avg8hours  = Avg8Hours(
            
                avgCO = avgCO,
                avgNo2 = avgNo2,
                avgO3 = avgO3,
                avgPm1 = avgPm1,
                avgPm10 = avgPm10,
                avgPm2_5 = avgPm2_5,
                dateIni = di,
                idStation = idStation,
                timestamp = tt
                
            )
    
            avg8hours.save()
        self.stdout.write(self.style.SUCCESS('Datos importados de forma correcta '))