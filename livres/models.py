from django.db import models

class Livre(models.Model):
    titre = models.CharField(max_length=200)
    auteur = models.CharField(max_length=100)
    date_publication = models.DateField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.titre} par {self.auteur}"

class Emprunt(models.Model):
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    nom_emprunteur = models.CharField(max_length=100)
    date_emprunt = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom_emprunteur} a emprunté {self.livre.titre}"