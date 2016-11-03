"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url

from photo.views import *

urlpatterns = [

    # Example: /
    url(r'^$', AlbumLV.as_view(), name='index'),  #album_list.html

    # Example: /album/, same as /
    url(r'^album/$', AlbumLV.as_view(), name='album_list'),   #album_list.html

    # Example: /album/99/
    url(r'^album/(?P<pk>\d+)/$', AlbumDV.as_view(), name='album_detail'),  #album_detail.html

    # Example: /photo/99/
    url(r'^photo/(?P<pk>\d+)/$', PhotoDV.as_view(), name='photo_detail'),  #photo_detail.html

]

