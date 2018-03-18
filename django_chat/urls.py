from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    url(r'^message_center/', include('message_center.urls')),
    url(r'^admin/', admin.site.urls),
]
