from django.urls import path 
from . import views
from django.core.mail import send_mail

urlpatterns = [
    path('', views.home, name='home'),
    path('commands', views.commands, name='commands'),
    path('developer', views.developers, name='developer'),
    path('privacy', views.privacy_p, name='privacy')

    
]
