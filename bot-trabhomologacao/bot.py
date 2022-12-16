import time
import os
import shutil
from csv import DictReader
from pathlib import PurePath

try:
    def bot():
        with open('G:/00. Atualização TOTVS\diretorio.csv') as pastaorigem:
            reader = DictReader(pastaorigem)
            for linha in reader:
                orig = linha['origem']
                dest = linha['destino']
                nomeu = os.getenv("USERNAME")
                if os.path.exists(dest):
                    nome = PurePath(orig).name
                    dest = os.path.join(dest, nome)

                shutil.copytree(orig, dest)
                os.rename('C:\Smartclient_Algar\PROTHEUS HOMOLOGAÇÃO.lnk', 'C:/Users/' + nomeu + '/Desktop/PROTHEUS HOMOLOGAÇÃO.lnk')
                print(dest, 'Foi finalizada a copia')
                print('----------------')


    bot()

except Exception as e:
    print(e)
    time.sleep(20)
