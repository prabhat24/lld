import uuid

from django.db import models
from django.contrib import admin

from core import model_mixins
from django.utils.translation import gettext_lazy as _

class Category(model_mixins.FullAuditMixin):
    label = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.id} | {self.label}" 

class Author(model_mixins.FullAuditMixin):
    name = models.CharField(max_length=255, null=False, blank=False)
    metadata = models.JSONField(null=True, blank=True, verbose_name="metadata information related to author like age, email")
    
    def __str__(self):
        return f"{self.id} | {self.name}" 

class Book(model_mixins.FullAuditMixin):

    title = models.CharField(max_length=255, null=False, blank=False)
    metadata = models.JSONField(null=True, blank=True, verbose_name="metadata information related to Book like description")
    isbn = models.CharField(max_length=20, null=True, blank=True)
    category = models.ManyToManyField(Category)
    author = models.ManyToManyField(Author, verbose_name="select author, search functionality is effected if author not present")

    def __str__(self):
        return f"{self.id} | {self.title}" 

class Rack(model_mixins.FullAuditMixin):
    location_identifier = models.CharField(unique=True, max_length=30, null=False, blank=False)

    def __str__(self):
        return f"{self.id} | {self.location_identifier}" 

class BookItem(model_mixins.FullAuditMixin):
    class StatusChoices(models.TextChoices):
        AVAILABLE = "AVAILABLE", _("Available")
        RESERVED = "RESERVED", _("Reserved by someone earlier")
        LOANED = "LOANED", _("Already borrowed")
        LOST = "LOST", _("Lost")
        DELETED = "DELETED", _("DELETED")
    class BookFormatChoices(models.TextChoices):
        HARDCOVER = "HARDCOVER", _("HARDCOVER")
        PAPERBACK = "PAPERBACK", _("PAPERBACK")
        AUDIO_BOOK = "AUDIO_BOOK", _("AUDIO_BOOK")
        EBOOK = "EBOOK", _("EBOOK")
        NEWSPAPER = "NEWSPAPER", _("NEWSPAPER")
        MAGAZINE = "MAGAZINE", _("MAGAZINE")
        JOURNAL = "JOURNAL", _("JOURNAL")
    slug = models.UUIDField(db_index=True, default=uuid.uuid4, null=False, blank=True, unique=True)
    rack = models.ForeignKey(Rack, null=True, blank=True, on_delete=models.SET_NULL)
    price = models.FloatField(null=False, blank=False)
    format = models.CharField(choices=BookFormatChoices, null=False, blank=False, default=BookFormatChoices.PAPERBACK, max_length=15)
    publication_date = models.DateField(null=True, blank=True)
    metadata = models.JSONField(null=True, blank=True, verbose_name="metadata information related to book item for future")
    book = models.ForeignKey(Book, null=False, blank=False, on_delete=models.PROTECT)
    status = models.CharField(choices=StatusChoices, max_length=15, default=StatusChoices.AVAILABLE)


