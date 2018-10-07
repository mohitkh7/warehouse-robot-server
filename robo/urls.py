from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('warehouse/<int:wid>', views.warehouse_details, name="warehouse-details"),
    path('create', views.create, name="create")
]
