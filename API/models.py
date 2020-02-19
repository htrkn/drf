from django.db import models

class Kurlar(models.Model):
    doviz_ismi = models.CharField(max_length=4)
    alis = models.FloatField(max_length=4)
    satis = models.FloatField(max_length=4)
    fark = models.FloatField()
    kur_kodu = models.CharField(max_length=22) # usd euro

def __str__(self):
    return self.doviz_ismi