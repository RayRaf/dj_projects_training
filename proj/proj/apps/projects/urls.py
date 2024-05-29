from django.urls import path
from . import views
from .views import ListView, CreateView, UpdateView

app_name = 'projects'

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.ProjectListView.as_view(), name='projects'),
    path('create/', views.ProjectCreateView.as_view(), name='project_create'),
    path('<int:pk>/edit', views.ProjectUpdateView.as_view(), name='project_edit'),
]

