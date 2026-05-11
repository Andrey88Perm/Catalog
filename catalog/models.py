from django.db import models
import os

def get_image_path(instance, filename):
    return os.path.join('equipment_images', filename)

class EquipmentType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=255)
    type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class EquipmentImage(models.Model):
    equipment = models.ForeignKey(Equipment, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_path)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.equipment.name} - {self.image.name}"