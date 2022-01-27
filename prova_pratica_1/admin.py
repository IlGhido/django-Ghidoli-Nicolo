from django.contrib import admin
from .models import Materia, Studente, Voto, Assenza

admin.site.register(Materia)
admin.site.register(Studente)
admin.site.register(Voto)
admin.site.register(Assenza)

# Register your models here.
