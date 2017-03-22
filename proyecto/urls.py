from django.conf.urls import patterns, include, url
from django.contrib import admin
#from django.contrib.auth.views import login, logout_then_login

admin.autodiscover()


urlpatterns = [
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls),

]
