from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('legos/', views.lego_index, name='lego-index'),
    path('legos/<int:lego_id>/', views.lego, name='lego-detail'),
    path('legos/create/', views.LegoCreate.as_view(), name='lego-create'),
    path('legos/<int:pk>/update/', views.LegoUpdate.as_view(), name='lego-update'),
    path('legos/<int:pk>/delete/', views.LegoDelete.as_view(), name='lego-delete'),
    path('wishlist/create/', views.WishlistCreate.as_view(), name='wishlist-create'),
    path('wishlist/', views.WishlistList.as_view(), name='wishlist-index'),
    path('wishlist/<int:pk>/', views.WishlistDetail.as_view(), name='wishlist-detail'),
    path('wishlist/<int:pk>/update/', views.WishlistUpdate.as_view(), name='wishlist-update'),
    path('wishlist/<int:pk>/delete/', views.WishlistDelete.as_view(), name='wishlist-delete'),
    path('accounts/signup/', views.signup, name='signup'),
]
