from django.urls import path

from . import views
#url patterns você escolhe como funcionará o link
urlpatterns = [
    path('', views.contact, name='contact'),
]

#slug é o que vai aparecer no link após clicar