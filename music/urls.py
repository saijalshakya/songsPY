# from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    # /music/
    url(r'^$', views.index, name="index"),

    # /music/1/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name="detail")
]