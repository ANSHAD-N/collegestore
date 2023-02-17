from django.urls import path

from . import views
from .views import get_course_ajax

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('form/', views.form, name='form'),
    path('get-course-ajax/', get_course_ajax, name="get_course_ajax"),

]