from django.db import models

# Create your models here.

# Portfolio 필드는 가게명/주소/사진
class Portfolio(models.Model):
    가게명 = models.CharField(max_length=200)
    주소 = models.CharField(max_length=400)
    사진 = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

# Comment 필드는 post(foreignkey부분)/작성자/내용/평점
class Comment(models.Model):


    grade_total= (
    (5, '5점'),

    (4, '4점'),

    (3, '3점'),

    (2, '2점'),

    (1, '1점'),
    )
    평점 = models.FloatField(
        choices=grade_total,
        default= 5
    )