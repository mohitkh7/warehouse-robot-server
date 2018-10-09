from django.urls import path

from . import views, views_robot, views_inventory

urlpatterns = [
    path('', views.index, name='index'),
    path('warehouse/create/', views.create_warehouse, name="create-warehouse"),
    path('warehouse/get/<int:wid>/', views.get_warehouse, name="get-warehouse"),
    path('warehouse/get/all/', views.get_warehouse_list, name="get-all-warehouse"),
    path('warehouse/update/<int:wid>/', views.update_warehouse, name="update-warehouse"),
    path('warehouse/delete/<int:wid>/', views.delete_warehouse, name="delete-warehouse"),

    path('robot/create/', views_robot.RobotCreate.as_view(), name="create-robot"),
    path('robot/get/all/', views_robot.RobotList.as_view(), name="get-all-robot"),
    path('robot/get/<int:pk>/', views_robot.RobotDetail.as_view(), name="get-robot"),
    path('robot/update/<int:pk>/', views_robot.RobotUpdate.as_view(), name="update-robot"),
    path('robot/delete/<int:pk>/', views_robot.RobotDelete.as_view(), name="delete-robot"),

    path('inventory/create/', views_inventory.InventoryCreate.as_view(), name="create-inventory"),
    path('inventory/get/all/', views_inventory.InventoryList.as_view(), name="get-all-inventory"),
    path('inventory/get/<int:pk>/', views_inventory.InventoryDetail.as_view(), name="get-inventory"),
    path('inventory/update/<int:pk>/', views_inventory.InventoryUpdate.as_view(), name="update-inventory"),
    path('inventory/delete/<int:pk>/', views_inventory.InventoryDelete.as_view(), name="delete-inventory"),
]
