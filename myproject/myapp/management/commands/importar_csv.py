import csv
from django.core.management.base import BaseCommand
from myapp.models import (
    Vulnerability,
    BiometricData
)  # Asegúrate de reemplazar `myapp` con el nombre de tu aplicación
from datetime import datetime

class Command(BaseCommand):
    help = "Importa datos desde un archivo CSV a la base de datos"

    def add_arguments(self, parser):
        parser.add_argument(
            "csv_file",
            type=str,
            help="La ruta al archivo CSV a importar",
        )

        # "./myapp/data_filtered.csv"
        "./myapp/biometric_data.csv"

    def handle(self, *args, **kwargs):
        csv_file = kwargs["csv_file"]

        with open(csv_file, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                BiometricData.objects.create(
                    datetime= parse_date(row['FECHA Y HORA']), #9/10/2024
                    id_number=row['NUMERO DE IDENTIFICACION'],
                    first_name=row['NOMBRES'],
                    last_name=row['APELLIDOS'],
                    phone=row['CELULAR'],
                    email=row['EMAIL'],
                    address=row['DIRECCION'],
                    company=row['COMPANIA'],
                    province=row['PROVINCIA'],
                    life_test_result=row['RESULTADO PRUEBA DE VIDA'],
                    document_check_result=row['RESULTADO DOCUMENT CHECK'],
                    facematch_result=row['RESULTADO FACEMATCH'],
                    biometric_result=row['RESULTADO BIOMETRIA']
                )
                # Vulnerability.objects.create(
                #     vendor_project=row["vendor_project"],
                #     product=row["product"],
                #     vulnerability_name=row["vulnerability_name"],
                #     date_added=row["date_added"],
                #     short_description=row["short_description"],
                #     required_action=row["required_action"],
                #     due_date=row["due_date"],
                #     grp=row["grp"],
                #     pub_date=row["pub_date"],
                #     cvss=row["cvss"],
                #     cwe=row["cwe"],
                #     vector=row["vector"],
                #     complexity=row["complexity"],
                #     severity=row["severity"],
                # )

        self.stdout.write(self.style.SUCCESS("Datos importados con éxito"))


def parse_date(date_str):
        formats = ['%d/%m/%Y', '%Y-%m-%d %H:%M:%S', '%m-%d-%Y']  # Agrega más si es necesario
        for fmt in formats:
            try:
                return datetime.strptime(date_str, fmt)
            except ValueError:
                continue
        return None  # Retorna None si ningún formato coincide