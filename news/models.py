from django.db import models

class Giornalista(models.Model):
    """ modello generico di un giornalista """
    nome = models.CharField(max_length=20)
    cognome = models.CharField(max_length=20)

    #def __str__(self):
        #return self.nome + " " + self.cognome

    class Meta:
        verbose_name = "Giornalista"
        verbose_name_plural = "Giornalista"
    
class Articolo(models.Model):
    """ modello generico di un articolo """
    titolo = models.CharField(max_length=20)
    contenuto = models.TextField()
    giornalista = models.ForeignKey(Giornalista, on_delete=models.CASCADE, related_name="articoli")

    #def __str__(self):
        #return self.titolo
    
    class Meta:
        verbose_name = "Articolo"
        verbose_name_plural = "Articolo"

# Create your models here.