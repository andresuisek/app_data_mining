from rest_framework import generics
from .models import Vulnerability

# from .serializers import VulnerabilitySerializer
from rest_framework.parsers import FileUploadParser
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.response import Response

import csv
import io

import rapidminer
import os
import joblib

model_path = os.path.join(os.path.dirname(__file__), "decission_tree_model.pkl")
model = joblib.load(model_path)

# rm_home = "C:/Program Files/RapidMiner/RapidMiner Studio"
# connector = rapidminer.Studio(rm_home, rm_stdout=open(os.devnull, "w"))
# score_path = "//Local Repository/project_data_analysis/process/Decision Tree/score"


class SeverityCountView(APIView):
    def get(self, request):
        severity_counts = (
            Vulnerability.objects.values("severity")
            .annotate(count=Count("severity"))
            .order_by("severity")
        )
        return Response(severity_counts)


class SeverityVsCVSSChart(APIView):
    def get(self, request):
        data = [
            {"severity": item.severity, "cvss": item.cvss}
            for item in Vulnerability.objects.all()
        ]
        return Response(data)


class PredictionView(APIView):
    def post(self, request):
        life_test_result = request.data.get("life_test_result")
        document_check_result = request.data.get("document_check_result")
        facematch_result = request.data.get("facematch_result")
        date_year = request.data.get("date_year")
        date_month = request.data.get("date_month")
        date_day = request.data.get("date_day")

        # Convert categorical values to numerical if needed
        life_test_result = 0 if life_test_result == "Approved" else 1
        document_check_result = 0 if document_check_result == "Approved" else 1
        facematch_result = int(facematch_result)

        value_to_predict = [
            life_test_result,
            document_check_result,
            facematch_result,
            # date_year,
            # date_month,
            # date_day,
        ]

        prediction = model.predict([value_to_predict])
        print(prediction)

        return Response({"prediction": prediction[0]})


class UploadCSVAPIView(APIView):
    # parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        file_obj = request.FILES["file"]
        if not file_obj.name.endswith(".csv"):
            return Response({"error": "File is not a CSV"}, status=400)

        try:
            rm_home = "C:/Program Files/RapidMiner/RapidMiner Studio"
            connector = rapidminer.Studio(rm_home, rm_stdout=open(os.devnull, "w"))
            score_path = (
                "//Local Repository/project_data_analysis/process/Decision Tree/score"
            )

            decoded_file = file_obj.read().decode("utf-8")
            data = io.StringIO(decoded_file)

            results = connector.run_process(
                score_path,
                inputs=data,
            )
            # C:/Users/andre/OneDrive/Desktop/rapidminer/data.csv

            # # Procesar el archivo CSV
            # csv_data = []
            # # decoded_file = file_obj.read().decode("utf-8").splitlines()
            # # reader = csv.DictReader(decoded_file)

            # for row in reader:
            #     # Aquí puedes procesar cada fila del CSV como desees
            #     csv_data.append(row)

            # Ejemplo de respuesta con los datos procesados
            return Response({"data": str(results["prediction(severity)"])})
        except Exception as e:
            return Response({"error": str(e)}, status=400)


# class VulnerabilityListCreateView(generics.ListCreateAPIView):
#     queryset = Vulnerability.objects.all().order_by("-date")
#     serializer_class = VulnerabilitySerializer

from rest_framework import generics
from .models import BiometricData
from .serializers import BiometricDataSerializer

class BiometricDataListView(generics.ListAPIView):
    queryset = BiometricData.objects.all()
    serializer_class = BiometricDataSerializer

class BiometricLifeTestResultsView(APIView):
    def get(self, request):
        data = (
            BiometricData.objects.values('life_test_result')
            .annotate(count=Count('life_test_result'))
            .order_by('life_test_result')
        )
        return Response(data)

class BiometricFacematchResultsView(APIView):
    def get(self, request):
        data = (
            BiometricData.objects.values('facematch_result')
            .annotate(count=Count('facematch_result'))
            .order_by('facematch_result')
        )
        return Response(data)

class BiometricResultsView(APIView):
    def get(self, request):
        data = (
            BiometricData.objects.values('biometric_result')
            .annotate(count=Count('biometric_result'))
            .order_by('biometric_result')
        )
        return Response(data)