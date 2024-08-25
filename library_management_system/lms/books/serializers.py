from rest_framework import serializers

from .models import BookItem, Author, Rack, Book, Category

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

class RackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rack
        fields = ['location_identifier']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'isbn', ]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["label"]


class BookItemSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(source="book.author", many=True, read_only=True)
    rack_name = serializers.CharField(source="rack.location_identifier", read_only=True)
    book_title = serializers.CharField(source="book.title", read_only=True)
    isbn = serializers.CharField(source="book.isbn", read_only=True)
    subject = CategorySerializer(source='book.category', read_only=True, many=True)
    class Meta:
        model = BookItem
        fields = ('id', 'price', 'format', 'publication_date', 'authors', 'rack_name', 'book_title', 'isbn', 'subject')

# class StatusChoices(models.TextChoices):
#     AVAILABLE = "AVAILABLE", _("Available")
#     RESERVED = "RESERVED", _("Reserved by someone earlier")
#     LOANED = "LOANED", _("Already borrowed")
#     LOST = "LOST", _("Lost")
#     DELETED = "DELETED", _("DELETED")
# class BookFormatChoices(models.TextChoices):
#     HARDCOVER = "HARDCOVER", _("HARDCOVER")
#     PAPERBACK = "PAPERBACK", _("PAPERBACK")
#     AUDIO_BOOK = "AUDIO_BOOK", _("AUDIO_BOOK")
#     EBOOK = "EBOOK", _("EBOOK")
#     NEWSPAPER = "NEWSPAPER", _("NEWSPAPER")
#     MAGAZINE = "MAGAZINE", _("MAGAZINE")
#     JOURNAL = "JOURNAL", _("JOURNAL")
# rack = models.ForeignKey(Rack, null=True, blank=True, on_delete=models.SET_NULL)
# price = models.FloatField(null=False, blank=False)
# format = models.CharField(choices=BookFormatChoices, null=False, blank=False, default=BookFormatChoices.PAPERBACK, max_length=15)
# publication_date = models.DateField(null=True, blank=True)
# metadata = models.JSONField(null=True, blank=True, verbose_name="metadata information related to book item for future")
# book = models.ForeignKey(Book, null=False, blank=False, on_delete=models.PROTECT)
# status = models.CharField(choices=StatusChoices, max_length=15, default=StatusChoices.AVAILABLE)