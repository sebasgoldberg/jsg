from django.conf.urls import include, url

from django.contrib import admin
import default.urls
from django.views.static import serve
from django.conf import settings

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'jsg.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(default.urls)),
    url(r'^media/(?P<path>.*)$', serve,
      {'document_root': settings.MEDIA_ROOT}),
]
