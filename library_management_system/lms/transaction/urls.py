from django.urls import path
from .views import *

urlpatterns = [
    path("lend-book/<uuid:id>", LendBook.as_view(), name='lend-book'),
    path("return-book/<uuid:item_slug>", ReturnBook.as_view(), name='return-book'),
    path("renew-book/<uuid:id>", RenewBook.as_view(), name='renew-book')
]