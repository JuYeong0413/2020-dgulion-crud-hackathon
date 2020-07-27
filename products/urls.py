from django.urls import path
from .views import *

app_name="products"
urlpatterns = [
    path('', main, name="main"),
    path('new/', create, name="create"),
    path('<int:product_id>/', show, name="show"),
    path('<int:product_id>/edit/', update, name="update"),
    path('<int:product_id>/delete/', delete, name="delete"),
]