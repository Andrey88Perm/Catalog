from django.db import models

class EquipmentType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=255)
    type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name