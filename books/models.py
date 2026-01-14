from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'
    )
    year = models.IntegerField()
    cover = models.ImageField(upload_to='cover/')
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.title} - {self.author.name}"

# Create your models here.
