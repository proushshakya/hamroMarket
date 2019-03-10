from django.contrib import admin  
from django.urls import path  
from product import views  
urlpatterns = [
    path('product/', views.product),  
    path('show/', views.show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy), 
    path('getjson', views.getjson),
    path('raw_sql', views.raw_sql),
    path('pay', views.pay), 
]