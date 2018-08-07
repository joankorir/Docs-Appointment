from django.urls import path
from.import views
app_name='Proj' 
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('(?P<pk>[0-9]+)/',views.DetailView.as_view(),name='detail'),
    path('album/add/',views.AlbumCreate.as_view(),name='album-add'),
    path('album/(?P<pk>[0-9]+)/',views.AlbumUpdate.as_view(),name='album-update'),
    path('album/(?P<pk>[0-9]+)/delete/',views.AlbumDelete.as_view(),name='album-delete'),

    ]