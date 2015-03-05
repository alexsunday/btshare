from django.conf.urls import patterns, include, url

urlpatterns = patterns('web.views',
    # Examples:
    # url(r'^$', 'btshare.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'index'),
)
