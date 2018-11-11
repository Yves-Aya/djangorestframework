from django.db import models

# Create your models here.

class paradigm(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name





class language(models.Model):
     name = models.CharField(max_length=50)
     paradigm = models.ForeignKey(paradigm, on_delete=models.CASCADE)

     def __str__(self):
         return self.name

class programmer(models.Model):
    name = models.CharField(max_length=200)
    language =models.ManyToManyField(language)

    def __str__(self):
        return self.name