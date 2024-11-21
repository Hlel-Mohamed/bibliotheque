from django.urls import path
from .views import *

app_name = "livres"

urlpatterns = [
    path('', livres_list_view, name='livres_list'),
    path('ajouter/', ajouter_livre_view, name='ajouter_livre'),
    path('<int:livre_id>/', livres_detail_view, name='livres_detail'),
    path('<int:livre_id>/modifier/', update_livre_view, name='modifier_livre'),
    path('<int:livre_id>/emprunter/', emprunter_livre_view, name='emprunter_livre'),
    path('non-disponibles/', livres_non_disponibles_view, name='livres_non_disponibles'),
]