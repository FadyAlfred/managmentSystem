from django.urls import path

from . import views

urlpatterns = [
    path('product/', views.ProductAPIView.as_view(), name='products'),
    path('product/<int:pk>/', views.ProductDetailAPIView.as_view(), name='product_detail'),

    path('category/', views.CategoryAPIView.as_view(), name='categories'),
    path('category/<int:pk>/', views.CategoryDetailAPIView.as_view(), name='category_detail'),
    path('category/<int:pk>/children/', views.CategoryChildrenView.as_view(), name='list_category_children'),
]
