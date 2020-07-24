from django.urls import path
from .views import *

app_name="products"
urlpatterns = [
    path('', main, name="main"),
    path('new/', create, name="create"),
    path('<int:post_id>/', show, name="show"),
    path('<int:post_id>/edit/', update, name="update"),
    path('<int:post_id>/delete/', delete, name="delete"),
]