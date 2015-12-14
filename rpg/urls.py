from django.conf.urls import url
from rpg.views import *


urlpatterns = [
    url(r'^$', home.get, name='home'),
    url(r'^login/$', login.get, name='login'),
    url(r'^logout/$', logout.get, name='logout'),
    url(r'^login/submit/$', login.post, name='authenticate'),
    url(r'api/properties/$', properties.select, name='properties'),
    url(r'api/thingy/$', properties.select, name='thingy'),
]

