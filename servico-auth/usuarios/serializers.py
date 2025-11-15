from django.contrib.auth.models import User
from rest_framework import serializers


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        # Cria o usuário com o password "hash" (criptografado)
        user = user.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )

        return user