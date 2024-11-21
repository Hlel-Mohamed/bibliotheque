from django.contrib import admin
from .models import Livre
from .models import Emprunt

@admin.register(Livre)
class LivreAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'disponible')
    list_filter = ('disponible', 'date_publication')
    search_fields = ('titre', 'auteur')
    ordering = ('date_publication',)

@admin.register(Emprunt)
class EmpruntAdmin(admin.ModelAdmin):
    list_display = ('livre', 'nom_emprunteur', 'date_emprunt')
    list_filter = ('date_emprunt',)
    search_fields = ('nom_emprunteur', 'livre__titre')
    ordering = ('date_emprunt',)
