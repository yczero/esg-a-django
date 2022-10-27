from wsgiref.validate import validator
from django.db import models
from django.core.validators import MaxValueValidator

class Restaurant(models.Model):
    """맛집"""
    name = models.CharField(max_length=30)
    description = models.TextField()
    avarage_score = models.PositiveSmallIntegerField(validators = [MaxValueValidator(5),])
    
    def get_absolute_url(self):

        # 향후에는 장고의 url reverse 기능을 활용하기
        return f"/blog/restaurants/{ self.pk }/"

    def __str__(self):
        # self.pk # int 숫자필드?
        return f'[{self.pk}] {self.name}'
   


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def get_absolute_url(self):

        # 향후에는 장고의 url reverse 기능을 활용하기
        return f"/blog/{ self.pk }/"

    def __str__(self):
        # self.pk # int 숫자필드?
        return f'[{self.pk}] {self.title}'
   

   