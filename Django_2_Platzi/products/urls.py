from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path("", views.ProductList.as_view(), name="hello"),
    path('product/<int:pk>/', views.ProductDetail.as_view(),
          name="detail" ),
    path(
      'product/new/',
      views.NewProductView.as_view(),
      name='new_product'
),
]