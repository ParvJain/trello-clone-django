from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=150)
    is_visible = models.BooleanField(default=True)
    user = models.ForeignKey(User)

    def __str__(self):
        return '{} - {} - {} - {}'.format(self.id, self.title, self.is_visible,
                                        self.user.id)

    class Meta:
        ordering = ['-id']

class Task(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    is_visible = models.BooleanField(default=True)
    weight = models.FloatField()
    category = models.ForeignKey(Category, related_name="tasks",
                                    on_delete=models.CASCADE)


    def __str__(self):
        return '{} - {} - {} - {} - {} - {}'.format(
                                                self.id, self.title,
                                                self.description,
                                                self.is_visible, self.weight,
                                                self.category.id)

    class Meta:
        ordering = ['-weight']
