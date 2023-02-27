from django.urls import path

from . import views
#url patterns você escolhe como funcionará o link
urlpatterns = [
    path('', views.BlogListView.as_view(),name='home'),
    path('post/teste/', views.hello, name='hello'),
    path('post/new/', views.BlogCreateView.as_view(),name='post_new'), #ativar o modo de visualização de cada post
    path('post/<slug:slug>/', views.BlogDetailView.as_view(),name='post_detail'), #ativar o modo de visualização de cada post
    path('post/<int:pk>/edit/', views.BlogUpdateView.as_view(),name='post_edit'), #ativar o modo de visualização de cada post
    path('post/<int:pk>/delete/', views.BlogDeleteView.as_view(),name='post_delete'),
    
]

#slug é o que vai aparecer no link após clicar