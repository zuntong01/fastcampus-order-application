
from django.urls import path
from delivery import views

urlpatterns = [
    path('delivery/', views.delivery, name="delivery"),
]


