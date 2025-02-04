from django.db import models


class BiometricData(models.Model):
    datetime = models.DateTimeField(null=True, blank=True)  # FECHA Y HORA
    id_number = models.CharField(
        max_length=20, null=True, blank=True
    )  # NUMERO DE IDENTIFICACION
    first_name = models.CharField(max_length=100, null=True, blank=True)  # NOMBRES
    last_name = models.CharField(max_length=100, null=True, blank=True)  # APELLIDOS
    phone = models.CharField(max_length=15, null=True, blank=True)  # CELULAR
    email = models.EmailField(null=True, blank=True)  # EMAIL
    address = models.CharField(max_length=200, null=True, blank=True)  # DIRECCION
    company = models.CharField(max_length=100, null=True, blank=True)  # COMPANIA
    province = models.CharField(max_length=100, null=True, blank=True)  # PROVINCIA
    life_test_result = models.CharField(
        max_length=50, null=True, blank=True
    )  # RESULTADO PRUEBA DE VIDA
    document_check_result = models.CharField(
        max_length=50, null=True, blank=True
    )  # RESULTADO DOCUMENT CHECK
    facematch_result = models.CharField(
        max_length=50, null=True, blank=True
    )  # RESULTADO FACEMATCH
    biometric_result = models.CharField(
        max_length=50, null=True, blank=True
    )  # RESULTADO BIOMETRIA

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
