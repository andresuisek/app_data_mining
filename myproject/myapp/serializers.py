from rest_framework import serializers
from myapp.models import Vulnerability, BiometricData


# class VulnerabilitySerializer(serializers.ModelSerializer):
#     key = serializers.SerializerMethodField()
#     date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)

#     class Meta:
#         model = Vulnerability
#         fields = "__all__"

#     def get_key(self, obj):
#         return obj.id

class BiometricDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BiometricData
        fields = '__all__'