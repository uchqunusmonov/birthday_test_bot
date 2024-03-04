from django.db import models


class TelegramUser(models.Model):
    user_id = models.CharField(max_length=120, unique=True)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='images/employees/')
    birthday = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

