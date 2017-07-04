from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^album/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^album/add/$', views.AlbumCreate.as_view(), name='add-album'),
    # album/2/
    url(r'^album/(?P<pk>[0-9]+)/update/$', views.AlbumUpdate.as_view(), name='update-album'),
    # music/album/2/delete
    url(r'^album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='delete-album'),
    # music/song/
    url(r'^song/add/$', views.SongCreate.as_view(), name='add-song'),
    url(r'^album/(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite')
]