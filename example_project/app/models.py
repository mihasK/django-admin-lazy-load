from django.db import models
from random import randrange
from functools import partial

# Create your models here.

class SomeThing(models.Model):
    
    number = models.IntegerField(default=partial(randrange, 0, 100))
    
    is_ok = models.BooleanField(default=True)
    
    @property
    def exponent(self):
        return (2**self.number) % 10**10