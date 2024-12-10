from django.db import models

class Formula(models.Model):
    name = models.CharField(max_length=100)
    expression = models.TextField(help_text="Use Python expressions. Ex: 'a + b * c'")

    def __str__(self):
        return self.name


class DataSet(models.Model):
    name = models.CharField(max_length=100)
    a = models.FloatField()
    b = models.FloatField()
    c = models.FloatField()

    def __str__(self):
        return self.name
