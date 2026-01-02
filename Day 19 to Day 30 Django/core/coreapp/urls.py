from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name="contact"),
    path('add/', views.add_student),
    path('students/', views.student_list, name='student_list'),
]