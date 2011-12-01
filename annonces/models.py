from django.db import models

class Departements(models.model):
    """
    Les Departements du pays
    """
    name = models.CharField(max_length=100, unique=True)
    def __unicode__(self):
        return self.name
class Villes(models.model):
    """
    Les villes par departements
    """
    name = models.CharField(max_length=150)
    departement = models.ForeignKey('Departement')
    def __unicode__(self):
        return self.name
    
class TypeAnnonces(models.model):
    """
    Les types d'annonces
    """
    type = models.CharField(max_length=150, unique=True)
    isactive = models.BooleanField()
    def __unicode__(self):
        return self.type
    
class Annonces(models.model):
    """
    Les annonces à publier
    """
    ATTENTE = 0
    INVALIDE = 1
    ACTIVE = 2
    INNACTIVE = 3
    STATUS = ((ATTENTE, ('attente')), (INVALIDE, ('invalide')), (ACTIVE, ('active')), (INNACTIVE, ('innactive')))
    titre = models.CharField(max_length=300)
    corps = models.TextField()
    crea_date = models.DateTimeField(auto_now_add=True)
    val_date = models.DateTimeField(auto_now=True)
    prix = models.CharField(max_length=20)
    status = models.IntegerField(_('status'), choices=STATUS, default=ATTENTE)
    categories = models.ForeignKey('Categories')
    utilisateurs = models.ForeignKey('Utilisateurs')
    typeAnnonces = models.ForeignKey('TypeAnnonces')
    def __unicode__(self):
        return self.titre

class Categories(models.model):
    """
    Les catégories d'annonces
    """
    name = models.CharField(max_length=150)
    isactive = models.BooleanField()
    def __unicode__(self):
        return self.titre

class Utilisateurs(models.model):
    """
    Les utilisateurs
    """
    nom = models.CharField(max_length=150)
    email = models.EmailField()
    tel = models.CharField(max_length=8)
    visible = models.BooleanField()
    typeUtilisateurs = models.ForeignKey('TypeUtilisateurs')
    def __unicode__(self):
        return self.nom
    

class TypeUtilisateurs(models.model):
    """
    Le type d'utilisateurs
    """
    type = models.CharField(max_length=150)
    def __unicode__(self):
        return self.type
    
class Photos(models.model):
    """
    Les photos des annonces
    """
    photo = models.ImageField(upload_to='annonces_photos/%d'%self.id, blank=True)
    annonces = models.ForeignKey('Annonces')
