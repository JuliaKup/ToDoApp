from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views import generic
from django.views.generic import TemplateView
from django.forms import inlineformset_factory
from django.utils import timezone

from tasks.models import Task, User, Project, Comment
from django.contrib.auth.models import User
from tasks.forms import TaskForm, CommentForm, TaskStatusForm

def index(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			form = TaskStatusForm(request.POST)
			if form.is_valid():
				task = Task.objects.get(pk = form.cleaned_data['task_id'])
				task.status = not task.status
				task.save()
				return HttpResponseRedirect('/tasks/')
		else:
			tasks = Task.objects.filter(user = request.user).order_by('due_date')
			projects = Project.objects.filter(user = request.user).order_by('due_date')
			form = TaskStatusForm()
			content = {
				'tasks_list': tasks,
				'projects_list': projects,
				'form': form,
			}
			return render(request, 'tasks/index.html', content)
	else:
		return HttpResponseRedirect("/login/")	

def detail(request, pk):
	try:
		task = Task.objects.get(pk=pk)
	except Task.DoesNotExist:
		return HttpResponseRedirect("/tasks/")
	if request.user == task.user:
		if request.method == "POST":
			commentform = CommentForm(request.POST)
			if commentform.is_valid():
				comment = commentform.save(commit=False)
				comment.user = request.user
				comment.task = task
				comment.save()
				return HttpResponseRedirect("/tasks/" + str(pk) + "/")
		else:
			commentform = CommentForm()
			comments = Comment.objects.filter(task = task)
			context = {
				'commentform': commentform,
				'task': task,
				'comments': comments,
			}
			return render(request, 'tasks/detail.html', context)
	else:
		return HttpResponseRedirect("/login/")

def create(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			form = TaskForm(request.POST)
			if form.is_valid():
				task = form.save(commit=False)
				task.user = request.user
				task.creation_date = timezone.now()
				task.save()
				return HttpResponseRedirect("/tasks/")
		else:
			form = TaskForm()
		return render(request, 'tasks/create.html', {'form': form})
	else:
		return HttpResponseRedirect("/login/")

