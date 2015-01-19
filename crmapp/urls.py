from django.conf.urls import patterns, include, url

from marketing.views import HomePage

urlpatterns = patterns('',
    # Marketing pages
    url(r'^$', HomePage.as_view(), name="home"),
    url(r'^signup/$',
        'crmapp.subscribers.views.subscriber_new', name='sub_new'
    ),
)
