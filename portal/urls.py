from django.contrib import admin
from django.conf.urls import include, url


admin.autodiscover()


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('rpg.urls', namespace='rpg')),
]
