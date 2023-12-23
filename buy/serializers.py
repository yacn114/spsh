from rest_framework import serializers
from buy.models import txtmodel
class buySerializers(serializers.Serializer):
    class Meta:
        model = txtmodel
        fields = '__all__'