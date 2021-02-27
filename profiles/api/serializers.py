from rest_framework import serializers
from profiles.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'pk',
            'user',
            'mobile',
            'email',
        ]
        read_only_fields = ['pk', 'user']