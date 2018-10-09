from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('warehouse/create/', views.create_warehouse, name="create-warehouse"),
    path('warehouse/get/<int:wid>/', views.get_warehouse, name="get-warehouse"),
    path('warehouse/get/all/', views.get_warehouse_list, name="get-all-warehouse"),
    path('warehouse/update/<int:wid>/', views.update_warehouse, name="update-warehouse"),
    path('warehouse/delete/<int:wid>/', views.delete_warehouse, name="delete-warehouse"),

    path('create', views.create, name="create")
]
