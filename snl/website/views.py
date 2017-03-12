from django.shortcuts import render
from django.http import HttpResponse

# Attractive Main page
def index(request):
	return HttpResponse("This is Saturday Night Live!")

# Display all seasons
def all_seasons(request):
	return HttpResponse("List of all seasons is as below:")

# Details in a season
def season(request,sid):
	return HttpResponse("Details about season: "+sid+" and list of all episode in it");

# Display all episodes sorted in some order
def all_episodes(request):
	return HttpResponse("List of all episode")

# EpisodeX
def episode(request,eid):
	return HttpResponse("Episode description and titles in episode: "+eid)

# Title
def title(request,tid):
	return HttpResponse("Title description with details of host cast and crew: "+tid)

# actors
def all_actors(request):
	return HttpResponse("Display all actors")

# actorX
def actor(request,aid):
	aid = aid.replace('_',' ')
	return HttpResponse("Actor: "+aid+" and his shows")

# popular episodes
def popular(request):
	return HttpResponse("Popular episodes with their ratings")