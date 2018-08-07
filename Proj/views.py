from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render,redirect,reverse
from django.views.generic import View
from.models import Album
from django.views import generic

class IndexView(generic.ListView):
	template_name='Proj/index.html'
	context_object_name='all_albums'
	def get_queryset(self):
	 	return Album.objects.all()
class DetailView(generic.DetailView):
    model=Album
    template_name='Proj/detail.html'	
class AlbumCreate(CreateView):
    model=Album 	
    fields=['artist','album_title','genre','album_logo']
class AlbumUpdate(UpdateView):
	model=Album
	fields=['artist','album_title','genre','album_logo']
class AlbumDelete(DeleteView):
	model=Album
	def get_success_url(self):
		return reverse('Proj:index')

