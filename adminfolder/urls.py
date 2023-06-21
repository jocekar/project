from django.urls import path
from adminfolder import views

urlpatterns = [
    path('backend/', views.backend, name='homepage'),
    path('backendedit/<str:pk>/', views.backend_edit, name='editbackendbackendpage'),
    path('backenddelete/<str:pk>/', views.backend_delete, name='deletebackendpage'),

    path('about/', views.about, name='aboutpage'),
    path('aboout-edit/<str:pk>/', views.about_edit, name='abouteditpage'),
    path('about-views/<str:pk>/', views.about_views, name='about-viewspage'),
    path('about-delete/<str:pk>/', views.about_delete, name='aboutdeletepage'),

    path('skill', views.skill, name='skillpage'),
    path('ski-edit/<str:pk>/', views.sk_edit, name='skil-edpage'),
    path('ski-del/<str:pk>/', views.skl_del, name='ski-delpage'),

    path('category/', views.category, name='categorypage'),
    path('category-edit/<str:pk>/', views.category_edit, name='category-editpage'),
    path('category-delete/<str:pk>/', views.category_delete, name='category-deletepage'),

    path('image/', views.image, name='imagepage'),
    path('image-edit/<str:pk>/', views.image_edit, name='image-editpage'),
    path('image-views/<str:pk>/', views.image_views, name='image-viewspage'),
    path('image-delete/<str:pk>/', views.image_delete, name='image-delete'),

    path('music/', views.music, name='musicpage'),

    path('song/', views.song, name='songpage'),
    path('song-ed/<str:pk>/', views.songedit, name='songeditpage'),
    path('song-del/<str:pk>/', views.songdelete, name='song-d-p'),
    

]
