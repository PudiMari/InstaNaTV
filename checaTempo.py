from datetime import datetime, timedelta
from pathlib import Path
import os
from datetime import datetime

fmt = '%d-%m-%Y'

dataDoDiretorio = os.path.getmtime("/content/2022-08-15_12-38-50_UTC_2.jpg")

dataArquivo = datetime.fromtimestamp(dataDoDiretorio)

dataHoje = datetime.today()

print(dataHoje)
print(dataArquivo)

quantidade_dias = abs((dataHoje - dataArquivo).days)

print(quantidade_dias)

