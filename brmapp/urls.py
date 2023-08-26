from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path("",home),
    path("viewbook",viewbook),
    path("add-book",add_book),
    path("delete-book/<int:book_id>",delete_book),
    path('edit-book/<int:book_id>',edit_book),
    path('do-edit-book/<int:book_id>',do_edit_book),
    path('show-book/<int:book_id>',show_book)
]