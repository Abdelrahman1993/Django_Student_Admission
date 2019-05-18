from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.user_login, name="user_login"),
    path('logout/', views.user_logout, name="user_logout"),
    path('register/', views.register, name="register"),
    path('dashboard/<semester>/', views.dashboard, name="dashboard"),
    path('remove/<int:subject_id>/<semester>/', views.remove_subject, name="remove_subject"),
    path('add/<int:subject_id>/<semester>/', views.add_subject, name="add_subject")
]