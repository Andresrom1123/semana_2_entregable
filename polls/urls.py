from django.urls import path

from polls import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:classroom_id>/', views.get_student, name='student')
]
