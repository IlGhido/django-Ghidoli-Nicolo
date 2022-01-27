from django.db import models

class Materia(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Materia"
        verbose_name_plural = "Materia"

class Studente(models.Model):
    nome = models.CharField(max_length=20)
    cognome = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Studente"
        verbose_name_plural = "Studenti"

class Voto(models.Model):
    numero = models.FloatField()
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name="voti")
    studente = models.ForeignKey(Studente, on_delete=models.CASCADE, related_name="voti")

    class Meta:
        verbose_name = "Voto"
        verbose_name_plural = "Voti"

class Assenza(models.Model):
    oreAssenza = models.BigIntegerField()
    studente = models.ForeignKey(Studente, on_delete=models.CASCADE, related_name="assenze")
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name="assenze")

    class Meta:
        verbose_name = "Assenza"
        verbose_name_plural = "Assenze"