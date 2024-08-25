from django.contrib import admin

from .models import *
# Register your models here.

class RackAdmin(admin.ModelAdmin):

    model = Rack
    list_display = (
                    'id',
                    'location_identifier',
                    )
  
class CategoryAdmin(admin.ModelAdmin):

    model = Category
    list_display = (
                    'id',
                    'label',
                    )

class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = (
        'id',
        'title',
        'isbn',
        'category_label',
        'authors',
    )
    def category_label(self, obj):
      labels = [ i["label"] for i in list(obj.category.all()[:10].values("label")) ]
      return labels

    def authors(self, obj):
        labels = [ i["name"] for i in list(obj.author.all()[:5].values("name")) ]
        return labels


class BookItemAdmin(admin.ModelAdmin):
    model = BookItem
    list_display = (
        'id',
        'title',
        'authors',
        'category_label'
    )
    exclude=('slug',)
    def title(self, obj):
        return obj.book.title
    
    def category_label(self, obj):
        labels = [ i["label"] for i in list(obj.book.category.all()[:10].values("label")) ]
        return labels

    def authors(self, obj):
        labels = [ i["name"] for i in list(obj.book.author.all()[:5].values("name")) ]
        return labels

# admin registration
admin.site.register(BookItem, BookItemAdmin)
admin.site.register(Rack, RackAdmin)
admin.site.register(Author)
admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
 