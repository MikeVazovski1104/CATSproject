from django.db import models

class Guest(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    cat = models.ForeignKey('Pets', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f"first_name={self.first_name}\n last_name={self.last_name}\n"


class Pets(models.Model):
    name = models.CharField(max_length=30)
    achievements = models.ManyToManyField('Achievements')

    def __str__(self):
        return f"name={self.name}\n achievements={self.achievements}"

class Achievements(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    def __str__(self):
        return self.name
