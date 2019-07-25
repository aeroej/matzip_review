from django.db import models

# Create your models here.


#class Portfolio(models.Model):

class Comment(models.Model):
    grade_total= (
    (5, '5점'),

    (4, '4점'),

    (3, '3점'),

    (2, '2점'),

    (1, '1점'),
    )
    grade = models.FloatField(
        choices=grade_total,
        default= 5
    )