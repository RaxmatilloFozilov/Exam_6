from django.db import models

class Topic(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']



# class Person(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
#     phone_number = models.CharField(max_length=15)
#     email = models.EmailField()
#     address = models.CharField(max_length=255)
#     date_of_birth = models.DateField()


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
    #     search_fields = ('name', 'description')
