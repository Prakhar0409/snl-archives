from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$',views.index,name='index'),
	
	url(r'^seasons/$',views.all_seasons,name='all_seasons'),
	url(r'^season/(?P<sid>[0-9]+)$',views.season,name='season'),
	
	url(r'^episodes/$',views.all_episodes,name='all_episodes'),
	url(r'^episode/(?P<sid_eid>[0-9]+_[0-9]+)$',views.episode,name='episode'),
	
	url(r'^title/(?P<tid>[0-9]+)$',views.title,name='title'),
	
	url(r'^actors/$',views.all_actors,name='all_actors'),
	url(r'^actor/(?P<aid>[A-Za-z_]+)$',views.actor,name='actor'),
	
	url(r'^popular/$',views.popular,name='popular'),
]