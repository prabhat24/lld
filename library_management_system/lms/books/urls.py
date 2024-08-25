from django.urls import path
from .views import *

urlpatterns = [
    path("search/", SearchBook.as_view(), name='books'),
]