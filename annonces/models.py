from django.db import models
from PIL import Image
from StringIO import StringIO
from django.core.files.base import ContentFile
import os

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
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='annonces_photos/%d'%self.id, blank=True)
    annonces = models.ForeignKey('Annonces')
    def updateContent(field, name, img, fmt="JPEG"):
        fp = StringIO()
        img.save(fp, fmt, quality=128)
        cf = ContentFile(fp.getvalue())
        if field:
            os.remove(field.path)
            field.save(name=name, content=cf, save=False)

    #area tuple = left, upper, right, lower coordinates
    def save(self, area=CROP_SIZE, crop=False, noResizing=False):
        if noResizing:
            super(Photos, self).save()
            return

        imgFile = Image.open(self.photo.path)
        fmt = imgFile.format

        #Convert to RGB
        if imgFile.mode not in ('L', 'RGB'):
            imgFile = imgFile.convert('RGB')

        # make sure photo doesn't exceed our max photo size for the site
        resizeImg = imgFile.copy()
        resizeImg.thumbnail(MAX_PHOTO_SIZE, Image.ANTIALIAS)
        updateContent(self.photo, self.photo.name, resizeImg, fmt)

        thumbImg = imgFile.copy()
        if crop:
            thumbImg = thumbImg.crop(area)
            thumbImg.load()
            thumbImg = thumbImg.resize(THUMBNAIL_SIZE, Image.ANTIALIAS)
        else:
            thumbImg.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)

        updateContent(self.thumbnail, self.photo.name, thumbImg, fmt)

        super(Photo, self).save()

