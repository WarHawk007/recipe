from django.contrib.auth import get_user_model

from rest_framework import serializers
from core.tests.utils import create_test_user


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'name')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        return create_test_user(**validated_data)
