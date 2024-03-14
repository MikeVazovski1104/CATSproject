from rest_framework import serializers

from .models import Guest, Pets


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ('first_name', 'last_name', 'cat',)


