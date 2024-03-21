from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only' : True}
        }

    def save(self):
        password = self.validated_data['password']
        
        if User.objects.filter(email = self.validated_data['email']).exists():
            raise serializers.ValidationError({'Error': 'Ese email ya se encuentra registrado'})
        
        account = User(email=self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(password)
        account.save()

        return account