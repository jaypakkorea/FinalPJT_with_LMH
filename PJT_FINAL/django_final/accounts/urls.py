from django.urls import path
from . import views

app_name = 'profile'
urlpatterns = [
    path('<int:user_pk>/', views.profile),
    path('<int:user_pk>/follow/', views.follow),
    path('<int:user_pk>/update/', views.update_profile),
]
