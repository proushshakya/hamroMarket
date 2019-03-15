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
    path('api/get_products/', views.get_products, name="get_products"),
    path('api/pay/', views.PaymentView.as_view(), name="pay"), 
]