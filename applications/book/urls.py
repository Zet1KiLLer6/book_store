from django.urls import path
from applications.book.views import *

urlpatterns = [
    path("", ListBookView.as_view()),
    path("<int:pk>/", RetrieveBookView.as_view()),
    path("create/", CreateBookView.as_view()),
    path("update/<int:pk>/", UpdateBookView.as_view()),
    path("delete/<int:pk>/", DeleteBookView.as_view()),
]