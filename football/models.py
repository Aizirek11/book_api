from django.db import models


class CoachProfile(models.Model):
    experience_years = models.IntegerField()
    nationality = models.CharField(max_length=100)

    def __str__(self):
        return self.nationality


class Coach(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    img = models.ImageField(upload_to='img/')


    def __str__(self):
        return self.name



class Team(models.Model):
    name = models.CharField(max_length=200)
    coach = models.ForeignKey(
        Coach,
        on_delete=models.CASCADE,
        related_name='teams'
    )
    logo = models.ImageField(upload_to='img/')

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=100)
    age = models.IntegerField()
    img = models.ImageField(upload_to='img/')
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='players'
    )

    def __str__(self):
        return self.name



class Tournament(models.Model):
    name = models.CharField(max_length=200)
    teams = models.ManyToManyField(
        Team,
        related_name='tournaments'
    )
    address = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    time = models.TimeField()


    def __str__(self):
        return self.name
