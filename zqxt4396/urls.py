from django.conf.urls import include, url
from tools import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = (
    # Examples:
    url(r'^$', views.index, name='home'),
    url(r'^add/$', views.add, name='add'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
