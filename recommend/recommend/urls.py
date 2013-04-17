from django.conf.urls import patterns, include, url
from recommend_core import views as core_views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    url(r'^anime/(?P<pk>\d+)/?$', core_views.AnimePageView.as_view(), name='anime_page'),

    url(r'^$', include('recommend_core.urls')),

    url(r'^api/', include('recommend_api.urls')),

)
