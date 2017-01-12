from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^room/(?P<room_id>[0-9]+)/$', 'room.views.show_room' , name='room'),
    url(r'^user/' , views.user , name='user')
]