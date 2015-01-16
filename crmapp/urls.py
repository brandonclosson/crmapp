from django.conf.urls import patterns, include, url

from marketing.views import HomePage

urlpatterns = patterns('',
    # Marketing pages
    url(r'^$', HomePage.as_view(), name="home")
)
