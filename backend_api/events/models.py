from django.db import models

# Create your models here.


class Events(models.Model):
    evt_id = models.CharField(max_length=21)
    evt_name = models.CharField(max_length=51)
    evt_type = models.CharField(max_length=51)

    def __str__(self):
        return self.evt_name