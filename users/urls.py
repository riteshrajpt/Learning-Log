from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name = 'users'
urlpatterns = [
    # Login page.
    url('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
   
    # logout page
    url(r'^logout/$', views.logout_view, name='logout'),

    # Registration Page
    url(r'^register/$', views.register, name= 'register'),

    
]