from django.db import models
from random import randrange
from time import sleep
from functools import partial
# Create your models here.

class SomeThing(models.Model):
    
    number = models.IntegerField(default=partial(randrange, 0, 100))
    
    is_ok = models.BooleanField(default=True)
    
    @property
    def model_calculated_field(self):
        sleep(5)  # heavy query or calculation happens
        return 'Number is %s' % self.number