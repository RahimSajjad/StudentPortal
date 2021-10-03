from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Notes(models.Model):
    # Jokhn user delete hoa jabe tokhn Notes o delet hoa jabe database theke
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=5000)

    class Meta:
        verbose_name = "notes"
        verbose_name_plural = "notes"

    def __str__(self):
        return f"{self.title}--> {self.user}-->{self.description[0:75]}....."


# Homework database model
class Homeworks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    title = models.CharField(max_length=300)
    description = models.TextField()
    due = models.DateTimeField()
    is_finished = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Homeworks"
        verbose_name_plural = "Homeworks"

    def __str__(self):
        return f"{self.subject}--> {self.title}--> {self.user}-->{self.description[0:75]}.....-->{self.is_finished} -->{self.due}"


# Todo
class Todo(models.Model):
    # Jokhn user delete hoa jabe tokhn Notes o delet hoa jabe database theke
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    description = models.TextField()
    is_finished = models.BooleanField(default=False)

    class Meta:
        verbose_name = "todo"
        verbose_name_plural = "todo"

    def __str__(self):
        return f"{self.title}-->{self.description[0:75]}-->{self.user}-->{self.is_finished}"
