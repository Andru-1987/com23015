from django.db import models

# Create your models here.


class Vino(models.Model):
    nombre  =   models.CharField(max_length=100)
    cosecha =   models.DateField(blank=False, null=False)
    rating  =   models.DecimalField(max_digits=10, decimal_places=2)
    abv     =   models.DecimalField(max_digits=10, decimal_places=2)
    lugar   =   models.CharField(max_length=100)
    
    def __str__(self):
        return f"El vino es: {self.nombre} - Cosecha: {self.cosecha}"
    
    def get_fields(self):
        return [
            (field.verbose_name, field.value_from_object(self))
            for field in self.__class__._meta.fields[1:]
        ]