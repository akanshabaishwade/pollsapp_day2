from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone


# created Questions model for question and here is one field called title
class Questions(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Choice(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text


class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=12)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
    def __str__(self):
        return self.full_name()
