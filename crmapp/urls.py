from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

from marketing.views import HomePage

urlpatterns = patterns('',
    # Marketing pages
    url(r'^$', HomePage.as_view(), name="home"),
    
    url(r'^signup/$',
        'crmapp.subscribers.views.subscriber_new', name='sub_new'
    ),

    # Login/Logout URLs
    (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    (r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login/'}),

    # Account related URLs
    url(r'^account/list/$',
    	AccountList.as_view(), name="account_list"
    ),

    (r'^admin/', include(admin.site.urls)),
)
