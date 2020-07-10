from django.urls import path

from polls import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:student_id>/', views.get_student, name='student')
]
