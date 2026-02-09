from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('<str:username>/edit/', views.ProfileEditView.as_view(), name='edit'),
    path('<str:username>/follow', views.FollowView.as_view(), name='follow'),
    path('<str:username>/', views.ProfileDetail.as_view(), name='detail'),
]
