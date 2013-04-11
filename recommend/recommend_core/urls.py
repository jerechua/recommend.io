from django.conf.urls import patterns, include, url

from recommend_core import views as core_views

urlpatterns = patterns('',
    url(r'^$', core_views.LandingPageView.as_view(), name='landing_page'),

)
