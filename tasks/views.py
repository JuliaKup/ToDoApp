from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views import generic
from django.views.generic import TemplateView
from django.forms import inlineformset_factory


from tasks.models import Task, User, Project, Comment
from django.contrib.auth.models import User
from tasks.forms import TaskForm, CommentForm

def index(request):
	if request.user.is_authenticated():
		tasks = Task.objects.filter(user = request.user)
		return render(request, 'tasks/index.html', {'tasks_list': tasks})
	else:
		return HttpResponseRedirect("/login/")	

def detail(request, pk):
	try:
		task = Task.objects.get(pk=pk)
	except Task.DoesNotExist:
		return HttpResponseRedirect("/tasks/")
	if request.user == task.user:
		commentform = CommentForm()
		context = {
			'commentform': commentform,
			'task': task,
		}
		return render(request, 'tasks/detail.html', context)
	else:
		return HttpResponseRedirect("/login/")

def comment(request, pk):
	try:
		task = Task.objects.get(pk=pk)
	except Task.DoesNotExist:
		return HttpResponseRedirect("/tasks/")
	if request.user.is_authenticated():
		if request.method == "POST":
			form = CommentForm(request.POST)
			if form.is_valid():
				comment = form.save(commit=False)
				comment.user = request.user
				comment.task = task
				comment.save()
				return HttpResponseRedirect("/tasks/" + str(pk) + "/")
		else:
			commentform = CommentForm()
		return HttpResponseRedirect("/tasks/" + str(pk) + "/")
	else:
		return HttpResponseRedirect("/login/")


def create(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			form = TaskForm(request.POST)
			if form.is_valid():
				task = form.save(commit=False)
				task.user = request.user
				task.save()
				return HttpResponseRedirect("/tasks/")
		else:
			form = TaskForm()
		return render(request, 'tasks/create.html', {'form': form})
	else:
		return HttpResponseRedirect("/login/")

