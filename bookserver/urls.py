from django.contrib import admin
from django.urls import path
from .views import books_crud, customer_crud, Loans_crud,APIViews
urlpatterns = [
    path('Books/', books_crud),
    path('Books/add', APIViews.as_view()),
    path('Book/change/<id>', books_crud),
    path('Customers/', customer_crud),
    path('Customers/add', customer_crud),
    path('Customers/change/<id>', customer_crud),
    path('Loans/', Loans_crud),
    path('Loans/add', Loans_crud),
    path('Loans/change/<id>', Loans_crud),
    
]
