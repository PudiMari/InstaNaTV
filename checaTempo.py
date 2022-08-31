from datetime import datetime, timedelta
from pathlib import Path
import os
from datetime import datetime

fmt = '%d-%m-%Y'

dataDoDiretorio = os.path.getmtime("ifmtcuiabaoficial")

dataArquivo = datetime.fromtimestamp(dataDoDiretorio)

dataHoje = datetime.today()

print(dataHoje)
print(dataArquivo)

quantidade_dias = abs((dataHoje - dataArquivo).days)

print(quantidade_dias)

