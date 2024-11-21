from django.shortcuts import render, get_object_or_404, redirect
from .models import Livre, Emprunt

def livres_list_view(request):
    livres = Livre.objects.filter(disponible=True)
    return render(request, 'livres/listeLivres.html', {'livres': livres})

def livres_detail_view(request, livre_id):
    livre = get_object_or_404(Livre, id=livre_id)
    return render(request, 'livres/detailLivre.html', {'livre': livre})

def ajouter_livre_view(request):
    if request.method == 'POST':
        titre = request.POST['titre']
        auteur = request.POST['auteur']
        date_publication = request.POST['date_publication']
        Livre.objects.create(titre=titre, auteur=auteur, date_publication=date_publication)
        return redirect('livres:livres_list')
    return render(request, 'livres/ajouterLivre.html')

def update_livre_view(request, livre_id):
    livre = get_object_or_404(Livre, id=livre_id)
    if request.method == 'POST':
        titre = request.POST['titre']
        auteur = request.POST['auteur']
        date_publication = request.POST['date_publication']
        livre.titre = titre
        livre.auteur = auteur
        livre.date_publication = date_publication
        livre.save()
        return redirect('livres:livres_detail', livre_id=livre_id)
    return render(request, 'livres/modifierLivre.html', {'livre': livre})

def emprunter_livre_view(request, livre_id):
    livre = get_object_or_404(Livre, id=livre_id)
    if request.method == 'POST':
        nom_emprunteur = request.POST['nom_emprunteur']
        Emprunt.objects.create(livre=livre, nom_emprunteur=nom_emprunteur)
        livre.disponible = False
        livre.save()
        return redirect('livres:livres_detail', livre_id=livre_id)
    return render(request, 'livres/emprunterLivre.html', {'livre': livre})

def livres_non_disponibles_view(request):
    livres = Livre.objects.filter(disponible=False)
    return render(request, 'livres/livresNonDisponibles.html', {'livres': livres})