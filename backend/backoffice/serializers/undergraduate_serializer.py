from rest_framework import serializers
from ..models import Undergraduate

class UndergraduateSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Undergraduate        # product 모델 사용
        fields = '__all__'            # 모든 필드 포함