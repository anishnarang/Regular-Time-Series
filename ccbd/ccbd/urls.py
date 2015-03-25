from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
     url(r'^$', 'webapp.views.input', name='input'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^images/','webapp.views.images',name='images'),
    url(r'^about/','webapp.views.TimeSeries',name='about'),    
]
