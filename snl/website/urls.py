from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'website'
urlpatterns = [
	url(r'^$',views.index,name='index'),
	
	url(r'^seasons/$',views.all_seasons,name='all_seasons'),
	url(r'^season/(?P<sid>[0-9]+)$',views.season,name='season'),
	
	url(r'^episodes/$',views.all_episodes,name='all_episodes'),
	url(r'^episodes_ratings/$',views.all_episodes_ratings,name='all_episodes_ratings'),
	url(r'^episode/(?P<sid_eid>[0-9]+_[0-9]+)$',views.episode,name='episode'),
	
	url(r'^title/(?P<tid>[0-9]+)$',views.title,name='title'),

	url(r'^type/(?P<showtype>[A-Za-z\ ]+)$',views.type,name='type'),
	
	url(r'^actors/$',views.all_actors,name='all_actors'),
	url(r'^actor/(?P<aid>[A-Za-z_\ ]+)$',views.actor,name='actor'),
	
	url(r'^popular/$',views.popular,name='popular'),

	url(r'^test/$',views.test,name='test'),

	url(r'^index1/$',views.index1,name='index1'),
	url(r'^index2/$',views.index2,name='index2'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#if settings.DEBUG:
#	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)