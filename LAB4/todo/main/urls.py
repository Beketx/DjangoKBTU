from django.urls import path
from main import views

app_name='main'
urlpatterns = [
    path('', views.MainPage.as_view(), name='index'),
    path('<int:id>/completed/', views.GetFinished.as_view(), name='finished'),
    path('<int:id>/delete', views.delete, name='delete'),
    path('<int:id>/update', views.update, name='update'),
    path('add/', views.add, name='add')
]