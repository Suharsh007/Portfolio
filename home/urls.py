from django.contrib import admin
from django.urls import path, include
from home import views

# Django admin header customisation
admin.site.site_header = "Developer Portfolio"
admin.site.site_title = "Welcome to Dashboard"
admin.site.index_title ="Welcome to the portal"
urlpatterns = [
    
    path('', views.home, name='home'),
     path('about', views.about, name='about'),
      path('projects', views.projects, name='projects'),
      path('contact', views.contact, name='contact'),
]
