import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_oo.settings')
django.setup()

from objects_app.models import *

while True:
    option = int(input('Digita "1" para cadastrar um Log e "2" para visualizar os Logs: '))
    if option == 1:
        log = Log(text=input("Digita o texto para o log: "))
        log.save()
    elif option == 2:
        print("Logs no Banco de Dados: ")
        logs = Log.objects.all()
        for log in logs:
            print(f"\t{log.pk}: {log.text}")
    else:
        print("escolha outra opcao:")

