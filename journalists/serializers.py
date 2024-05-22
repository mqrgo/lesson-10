from rest_framework import serializers
from journalists import models


class Journalist(serializers.ModelSerializer):
    class Meta:
        model = models.Journalist
        fields = '__all__'
