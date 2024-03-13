from decimal import Decimal
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class InformationsInternaute(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, unique=True)
    addres = models.CharField(max_length=50)
    telephone = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name="internaute")

    # Ajoutez d'autres champs au besoin

    def __str__(self):
        return self.nom


# Appareils Model
class Appareil(models.Model):
    nom = models.CharField(max_length=50)
    type =  models.CharField(max_length=50, blank=True)
    cote = models.DecimalField(max_digits=5, decimal_places=2)
    power = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0)
    def __str__(self):
        return self.nom + "(" + str(self.cote) + ")"

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Appareil'
        verbose_name_plural = 'Appareils'
# Devis Model
class Devis(models.Model):
    internaute_temp = models.ForeignKey(InformationsInternaute, null=True, blank=True, on_delete=models.SET_NULL)
    date = models.DateField(auto_now_add=True)
    energie_T = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    def __str__(self):
        return str(self.energie_T)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Devis'
        verbose_name_plural = 'Deviss'
#Appareil_devis Model
class Devis_Appareil(models.Model):
    appareil  = models.ForeignKey("Appareil", on_delete=models.CASCADE)
    devis  = models.ForeignKey("Devis", on_delete=models.CASCADE)
    quantite = models.IntegerField()
    numHours = models.IntegerField(null=True, blank=True, default=0)
    power = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    energie_T = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Calculer la valeur de energie_T
        self.energie_T = Decimal(self.quantite) * Decimal(self.numHours) * Decimal(self.power)
        super().save(*args, **kwargs)

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Devis_Appareil'
        verbose_name_plural = 'Devis_Appareils'