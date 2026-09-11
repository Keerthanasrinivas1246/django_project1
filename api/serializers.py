from rest_framework import serializers 
from . models import *

class coupleSerializer(serializers.ModelSerializer):
    class Meta:
        model = couple 
        fields = '__all__'