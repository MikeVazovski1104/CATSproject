from django.db import models

class Guest(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return f"first_name={self.first_name}\n last_name={self.last_name}\n"

class Achievements(models.Model):
    ACHIEV = (
        ('СК', 'Супер кусь'),
        ('ПНШ', 'Прыжок на шкаф'),
    )
    name = models.CharField(max_length=3, choices=ACHIEV)

    def __str__(self):
        return self.get_name_display()

class Pets(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    achievements = models.ManyToManyField(Achievements)

    def __str__(self):
        return f"name={self.name}\n achievements={[achievement.name for achievement in self.achievements.all()]}"
