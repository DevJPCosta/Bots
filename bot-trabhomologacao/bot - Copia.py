import os
import shutil
from csv import DictReader
from pathlib import PurePath

with open('G:/001\diretorio.csv') as pastaorigem:
    reader = DictReader(pastaorigem)
    for linha in reader:
        orig = linha['origem']
        dest = linha['destino']
        nomeu = os.getenv("USERNAME")
        if os.path.exists(dest):
            nome = PurePath(orig).name
            dest = os.path.join(dest, nome)

        shutil.copytree(orig, dest)
        os.rename('C:\Smartclient_Algar\PROTHEUS HOMOLOGAÇÃO.lnk', 'C:/Users/'+nomeu+'/Desktop/PROTHEUS HOMOLOGAÇÃO.lnk')
        print(dest, 'Foi finalizada a copia')
        print('----------------')









#shutil.copy2(r'G:\001\Smartclient_Algar', 'C:\Smartclient_Algar')
#os.rename('G:/001\Smartclient_Algar', 'C:\Smartclient_Algar')



