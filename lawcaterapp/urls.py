from . import views
from django.urls import path
from .views import *
from django.urls import path,include
from django.views.generic import TemplateView


urlpatterns = [
    path('', homepage, name = 'home'),
    #  path('story/', Story, name = 'story'),



     path('post/<slug>/', detail, name = 'detail'),
      # path('blog/<id>', Blog, name = 'blog'),

    # path('post/<slug>/', post, name = 'post'),

      path("team/", team, name="team"),
     path("contact/", contact, name="contact"),

    #  path("sendmail/", sendmail, name="sendmail"),

    #  path('/sendmail/',TemplateView.as_view(template_name='home.html')),

      path('<slug:slug>/', postByCategory, name = 'category'),


]