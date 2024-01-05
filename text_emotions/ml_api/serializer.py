from rest_framework import serializers
from .models import FileModel


class FileSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = FileModel
        fields = '__all__'
