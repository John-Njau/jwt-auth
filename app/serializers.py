from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password')
        # not to return the password
        extra_kwargs = {'password': {'write_only': True}}

    # hashing password
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            name=validated_data['name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.set_password(validated_data.get('password', instance.password))
        instance.save()
        return instance