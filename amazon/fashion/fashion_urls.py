from django.urls import path
from fashion import views

urlpatterns = [
    path('home/', views.show_fashion),
]
