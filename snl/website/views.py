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
	cursor.execute('SELECT e.sid,e.eid,e.aired,(one+two+three+four+five+six+seven+eight+nine+ten) AS votes, round((one*1+two*2+three*3+four*4+five*5+six*6+seven*7+eight*8+nine*9+ten*10)::decimal/(one+two+three+four+five+six+seven+eight+nine+ten)::decimal,2) as avg_rating \
		 FROM episode AS e, rating AS r WHERE r.sid = %s AND e.sid = %s AND r.eid = e.eid ORDER BY sid DESC,eid',[sid,sid])
	# cursor.execute('SELECT * FROM episode WHERE sid=%s ORDER BY eid', [sid])
	episodes = cursor.fetchall()
	# print(episodes)
	return render(request,'website/season.html',{'sid':sid,'episodes':episodes})

# Display all episodes sorted in some order
def all_episodes(request):
	cursor = connection.cursor()
	cursor.execute('SELECT e.sid,e.eid,e.aired,(one+two+three+four+five+six+seven+eight+nine+ten) AS votes, round((one*1+two*2+three*3+four*4+five*5+six*6+seven*7+eight*8+nine*9+ten*10)::decimal/(one+two+three+four+five+six+seven+eight+nine+ten)::decimal,2) as avg_rating \
		 FROM episode AS e, rating AS r WHERE r.sid = e.sid AND r.eid = e.eid ORDER BY sid DESC,eid')
	episodes = cursor.fetchall()
	# print(episodes)
	return render(request,'website/episodes.html',{'episodes':episodes})

# Display all episodes sorted in some order
def all_episodes_ratings(request):
	cursor = connection.cursor()
	cursor.execute('SELECT e.sid,e.eid,e.aired,(one+two+three+four+five+six+seven+eight+nine+ten) AS votes, round((one*1+two*2+three*3+four*4+five*5+six*6+seven*7+eight*8+nine*9+ten*10)::decimal/(one+two+three+four+five+six+seven+eight+nine+ten)::decimal,2) as avg_rating \
		 FROM episode AS e, rating AS r WHERE r.sid = e.sid AND r.eid = e.eid ORDER BY avg_rating DESC,sid DESC,eid')
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
	tid_list = []
	for t in titles:
		tid_list.append(t[2])
	print(tid_list)
	cursor.execute('SELECT DISTINCT a.aid,a.name FROM actor AS a, actor_title AS at WHERE at.tid = ANY(%s) AND a.aid=at.aid ', [tid_list])
	actors = cursor.fetchall()
	
	#for ratings
	cursor.execute('SELECT  (one+two+three+four+five+six+seven+eight+nine+ten) AS votes, (one*1+two*2+three*3+four*4+five*5+six*6+seven*7+eight*8+nine*9+ten*10)/(one+two+three+four+five+six+seven+eight+nine+ten) as avg_rating, \
		 age18_29, age18_29_avg, age30_44, age30_44_avg, age45p, age45p_avg, age18m, age18m_avg, \
		non_us, non_us_avg, us,us_avg FROM rating WHERE sid=%s AND eid=%s', [sid,eid])
	rating = cursor.fetchone()
	# print(len(rating)) 
	rating = list(rating)
	for i in range(0,len(rating)):
		if rating[i] is None:
			rating[i]=0
	print(rating)
	# rating=rating_tmp
	return render(request,'website/episode.html',{'sid':sid,'eid':eid,'titles':titles,'actors':actors,'rating':rating})

def type(request,showtype):
	return HttpResponse("showtype "+showtype+" selected!")


# Title
def title(request,tid):
	print(tid)
	cursor = connection.cursor()
	cursor.execute('SELECT * FROM title WHERE tid=%s ', [tid])
	title = cursor.fetchone()
	print(title)
	cursor.execute('SELECT a.aid,isCast,name,type FROM actor_title AS at, actor AS a WHERE tid=%s AND at.aid = a.aid ', [tid])
	actors = cursor.fetchall()
	crew = []
	cast = []
	host = []
	music = []
	cameo = []
	unknown = []
	actor_show = []
	print(actors)
	for a in actors:
		# cursor.execute('SELECT * FROM actor_title AS at, title AS t WHERE aid=%s AND t.tid = at.tid', [a[3]])
		# shows = cursor.fetchall()
		if a[3]=='crew':
			crew.append(a)
		elif a[3]=='cast':
			cast.append(a)
		elif a[3]=='host':
			host.append(a)
		elif a[3]=='music':
			music.append(a)
		elif a[3]=='cameo':
			cameo.append(a)
		else:
			unknown.append(a)
	return render(request,'website/title.html',{'title':title,'cast':cast,'crew':crew,'host':host,
											'music':music,'cameo':cameo,'unknown':unknown,'actors':actors})


# actors
# For each actor show (name, id, if cast, number of titles, sort alphabetically)
def all_actors(request):
	cursor = connection.cursor()
	cursor.execute('SELECT * FROM actor ORDER BY LOWER(aid) DESC')
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
	cursor.execute('SELECT DISTINCT at.tid,t.name,t.type,at.type,t.sid,t.eid FROM actor_title AS at, title AS t WHERE aid=%s AND at.tid = t.tid ', [aid])
	titles = cursor.fetchall()
	# cursor.execute('SELECT t.tid,t.name,t.type,x.type,t.sid,t.eid FROM (SELECT at.type,at.tid FROM actor_title AS at,host as h WHERE h.aid=%s AND h.aid=at.aid) AS x, title AS t WHERE x.tid = t.tid ', [aid])
	# titles = cursor.fetchall()
	print(titles)
	num = len(titles)
	return render(request,'website/actor.html',{'actor': actor,'titles':titles,'num':num})

# popular episodes
def popular(request):
	return HttpResponse("Popular episodes with their ratings")

#search episodes or actors
def search(request):
	header_msg = 'none'
	episodes = []
	actor = []
	titles = []
	if request.method == 'POST':
		search_for = request.POST.get('search_for','null')
		search_param = request.POST.get('search_param','null')
		val = request.POST.get('x','null')
		print(search_for)
		if search_param == 'default':
			header_msg = 'Search filter not selected'
		elif search_param == 'null' or val=='null' or val=='':
			header_msg = 'Invalid search query'
		
		elif search_for=='episodes':
			print('Search by episode')
			val = '%' + val + '%'
			if search_param == 'host':
				cursor = connection.cursor()
				cursor.execute('SELECT DISTINCT e.sid,e.eid,e.aired,h.aid FROM host as h, episode as e WHERE aid ILIKE %s AND e.sid=h.sid AND e.eid = h.eid ORDER BY e.sid DESC,e.eid', [val])
				episodes = cursor.fetchall()
				print(episodes)
			elif search_param == 'actor' or search_param== 'music':
				cursor = connection.cursor()
				cursor.execute('SELECT DISTINCT e.sid,e.eid,e.aired,y.name from episode as e,title as t,(SELECT at.tid,x.name from (SELECT a.aid,a.name FROM actor AS a WHERE a.name ILIKE %s) as x, actor_title AS at WHERE at.aid = x.aid) as y WHERE t.tid=y.tid AND e.sid = t.sid AND e.eid = t.eid ORDER BY e.sid DESC,e.eid', [val])
				episodes = cursor.fetchall()
				print(episodes)
			elif search_param == 'title':
				cursor = connection.cursor()
				cursor.execute('SELECT DISTINCT e.sid,e.eid,e.aired,t.name from episode as e,title as t WHERE t.name ILIKE %s AND t.sid = e.sid AND t.eid = e.eid ORDER BY e.sid DESC,e.eid', [val])
				episodes = cursor.fetchall()
				print(episodes)
		elif search_for == 'titles':
			print('search by title')
			val = '%' + val + '%'
			if search_param == 'host':
				cursor = connection.cursor()
				cursor.execute('SELECT DISTINCT t.tid,t.name,t.type,t.sid,t.eid,h.aid FROM title as t,actor_title as at, host as h WHERE h.aid ILIKE %s AND at.aid=h.aid AND at.tid=t.tid AND t.sid=h.sid AND t.eid = h.eid', [val])
				titles = cursor.fetchall()
				print(titles)
			elif search_param == 'actor' or search_param== 'music':
				cursor = connection.cursor()
				cursor.execute('SELECT DISTINCT t.tid,t.name,t.type,t.sid,t.eid,y.name FROM title AS t, (SELECT at.tid,x.name FROM actor_title AS at, (SELECT a.aid,a.name from actor AS a WHERE a.name ILIKE %s) AS x WHERE at.aid=x.aid) AS y WHERE t.tid = y.tid', [val])
				titles = cursor.fetchall()
				print(titles)
			elif search_param == 'title':
				cursor = connection.cursor()
				cursor.execute('SELECT DISTINCT t.tid,t.name,t.type,t.sid,t.eid from title as t WHERE t.name ILIKE %s ORDER BY t.name ', [val])
				titles = cursor.fetchall()
				print(titles)
		elif search_for == 'actors':
			print('search by actor')
			val = '%' + val + '%'
			if search_param == 'host':
				cursor = connection.cursor()
				# print('SELECT DISTINCT a.aid,a.name FROM actor as a, host as h WHERE a.name ILIKE %s AND a.aid=h.aid', [val])
				cursor.execute('SELECT DISTINCT a.aid,a.name FROM actor as a, host as h WHERE a.name ILIKE %s AND a.aid=h.aid', [val])
				actors = cursor.fetchall()
				print(actors)
			elif search_param == 'actor' or search_param== 'music':
				cursor = connection.cursor()
				cursor.execute('SELECT DISTINCT a.aid,a.name FROM actor AS a WHERE a.name ILIKE %s ', [val])
				actors = cursor.fetchall()
				print(actors)
			elif search_param == 'title':
				cursor = connection.cursor()
				cursor.execute('SELECT DISTINCT a.aid,a.name from actor as a, (SELECT at.aid FROM actor_title as at, (SELECT t.tid FROM title as t WHERE t.name ILIKE %s) as x WHERE x.tid=at.tid) as y WHERE y.aid=a.aid ', [val])
				actors = cursor.fetchall()
				print(actors)
	return render(request,'website/search.html',{'header':header_msg,'episodes':episodes,'actors':actors,'titles':titles})