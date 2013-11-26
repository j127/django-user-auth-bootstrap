from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djusers.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^signup/$', 'authapp.views.signup_view'),
    url(r'^login/$', 'authapp.views.login_view'),
    url(r'^admin/', include(admin.site.urls)),
)
