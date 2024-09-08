from django.db import models


class Bd(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(default=' ')
    price = models.FloatField(default=0.0)
    published = models.DateTimeField(auto_now_add=True, db_index=True)



