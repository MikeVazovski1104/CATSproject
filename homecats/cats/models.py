from django.db import models
class Guest(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return f"first_name={self.first_name}\n last_name={self.last_name}\n"

class Pets(models.Model):
    Guest = models.ForeignKey(Guest, on_delete = models.CASCADE)
    name = models.CharField(max_length=30)
    achievement = models.ManyToManyField(Achievements)
    def __str__(self):
        return f"name={self.name}\n achievements={self.achievements}"

class Achievements(models.Model):
    ACHIEV = (
        ('СК', 'Супер кусь'),
        ('ПНШ', 'Прыжок на шкаф'),
    )
    achiev = models.CharField(max_length=3, choices=ACHIEV)