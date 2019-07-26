from django.db import models

# Create your models here.

# Portfolio 필드는 가게명/주소/사진
#class Portfolio(models.Model):

# Comment 필드는 포스트(foreignkey부분)/작성자/내용/평점
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