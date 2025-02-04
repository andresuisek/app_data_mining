from django.urls import path
from .views import (
    SeverityCountView,
    SeverityVsCVSSChart,
    UploadCSVAPIView,
    PredictionView,
    BiometricDataListView,
    BiometricLifeTestResultsView,
    BiometricFacematchResultsView,
    BiometricResultsView
)

urlpatterns = [
    path("severity-count/", SeverityCountView.as_view(), name="severity-count"),
    path(
        "severity-vs-cvss-chart/",
        SeverityVsCVSSChart.as_view(),
        name="severity-vs-cvss-chart",
    ),
    path("prediction/", PredictionView.as_view(), name="prediction"),
    path("upload-csv/", UploadCSVAPIView.as_view(), name="upload-csv"),
    path("biometric-data/", BiometricDataListView.as_view(), name="biometric-data"), 
    path("biometric-life-test-results/", BiometricLifeTestResultsView.as_view(), name="biometric-life-test-results"),
    path("biometric-facematch-results/", BiometricFacematchResultsView.as_view(), name="biometric-facematch-results"),
    path("biometric-results/", BiometricResultsView.as_view(), name="biometric-results"),  # Añade la nueva ruta
]