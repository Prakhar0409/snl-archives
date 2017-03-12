from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

# Attractive Main page
def index(request):
	return render(request,'website/index.html')

# Attractive Main page testing
def index1(request):
	return render(request,'website/index1.html')

# Attractive Main page testing
def index2(request):
	return render(request,'website/index2.html')


# Display all seasons
def test(request):
	cursor = connection.cursor()
	cursor.execute('SELECT * FROM season')
	seasons = cursor.fetchall()
	return render(request,'website/test.html',{'seasons':seasons})

# Display all seasons
def all_seasons(request):
	cursor = connection.cursor()
	cursor.execute('SELECT * FROM season')
	seasons = cursor.fetchall()
	return render(request,'website/seasons.html',{'seasons':seasons})

# Details in a season
def season(request,sid):
	cursor = connection.cursor()
	cursor.execute('SELECT * FROM episode WHERE sid=%s ORDER BY eid', [sid])
	episodes = cursor.fetchall()
	# print(episodes)
	return render(request,'website/season.html',{'sid':sid,'episodes':episodes})

# Display all episodes sorted in some order
def all_episodes(request):
	cursor = connection.cursor()
	cursor.execute('SELECT * FROM episode ORDER BY sid DESC,eid')
	episodes = cursor.fetchall()
	# print(episodes)
	return render(request,'website/episodes.html',{'episodes':episodes})

# EpisodeX
def episode(request,sid_eid):
	uid = sid_eid.split('_')
	sid = uid[0]
	eid = uid[1]
	cursor = connection.cursor()
	cursor.execute('SELECT * FROM title WHERE sid=%s AND eid=%s ORDER BY tid ', [sid,eid])
	titles = cursor.fetchall()

	print(titles)
	return render(request,'website/episode.html',{'sid':sid,'eid':eid,'titles':titles})

def type(request,showtype):
	return HttpResponse("showtype "+showtype+" selected!")


# Title
def title(request,tid):
	print(tid)
	cursor = connection.cursor()
	cursor.execute('SELECT * FROM title WHERE tid=%s ', [tid])
	title = cursor.fetchone()
	print(title)
	cursor.execute('SELECT * FROM actor_title WHERE tid=%s ', [tid])
	actors = cursor.fetchall()
	crew = cast = host = music = cameo = unknown = []
	for a in actors:
		if a[4]=='crew':
			crew.append(a)
		elif a[4]=='cast':
			cast.append(a)
		elif a[4]=='host':
			host.append(a)
		elif a[4]=='music':
			music.append(a)
		elif a[4]=='cameo':
			cameo.append(a)
		else:
			unknown.append(a)
	return render(request,'website/title.html',{'title':title,'cast':cast,'crew':crew,'host':host,
											'music':music,'cameo':cameo,'unknown':unknown,'actors':actors})


# actors
def all_actors(request):
	cursor = connection.cursor()
	cursor.execute('SELECT * FROM actor ORDER BY aid DESC')
	actors = cursor.fetchall()
	return render(request,'website/actors.html',{'actors': actors})

# actorX
def actor(request,aid):
	aid = aid.replace('_',' ')
	print(aid)
	cursor = connection.cursor()
	cursor.execute('SELECT * FROM actor WHERE aid=%s ', [aid])
	actor = cursor.fetchone()
	print(actor)
	cursor.execute('SELECT * FROM actor_title WHERE aid=%s ', [aid])
	titles = cursor.fetchall()
	return render(request,'website/actor.html',{'actor': actor,'titles':titles})
	return HttpResponse("Actor: "+aid+" and his shows")

# popular episodes
def popular(request):
	return HttpResponse("Popular episodes with their ratings")