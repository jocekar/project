from django.urls import path
from frontend import views

urlpatterns = [
    path('', views.frontend, name='frontendpage'),
    path('detail/<str:pk>/', views.portfolio_detail, name='portfilio-detailpage')
]
