from django.db import models


class Guest(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    cat = models.ForeignKey('Cat', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"first_name={self.first_name}\n last_name={self.last_name}\n"


class Achievements(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


class Cat(models.Model):
    name = models.CharField(max_length=30)
    achievements = models.ManyToManyField('Achievements', through='AchievementsCat')

    def __str__(self):
        return self.name


class AchievementsCat(models.Model):
    achievement = models.ForeignKey('Achievements', on_delete=models.CASCADE)
    cat = models.ForeignKey('Cat', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.achievement} {self.cat}'
