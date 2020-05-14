from django.urls import path
from .views import *

app_name = "libraryapp"

urlpatterns = [
    path('', home, name='home'),
    path('books/', book_list, name='books'),
    path('librarians/', list_librarians, name='librarians'),
    path('libraries/', library_list, name='libraries'),
]