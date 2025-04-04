from django.db import models


class Historia(models.Model):
    id = models.IntegerField(primary_key=True)
    paciente = models.CharField(max_length=100)
    cc=models.IntegerField()
    
    def __str__(self):
        return '%s' % (self.id)
