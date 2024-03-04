from .models import TelegramUser, Employee
from rest_framework import serializers
from datetime import datetime

today = datetime.now().date()


class TelegramUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = ('name', 'username', 'user_id', 'created_at')

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.username = validated_data.get('username', instance.username)
        instance.save()
        return instance


class EmployeeSerializer(serializers.ModelSerializer):
    position = serializers.SerializerMethodField()
    age = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'birthday', 'image', 'position', 'age']

    def get_position(self, obj):
        if obj.position:
            return {
                'id': obj.position.id,
                'name': obj.position.name
            }
        return None

    def get_age(self, obj):
        age = today.year - obj.birthday.year
        return age


class TelegramAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = ['user_id']


