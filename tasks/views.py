from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views import generic
from django.views.generic import TemplateView
from django.forms import inlineformset_factory
from django.utils import timezone
from datetime import timedelta

from tasks.models import Task, User, Project, Comment
from django.contrib.auth.models import User
from tasks.forms import TaskForm, CommentForm, TaskStatusForm, RemoveTaskForm

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
			overdue = Task.objects.filter(user = request.user, status = False).exclude(due_date__gt=timezone.now()).order_by('due_date')
			week_tasks = Task.objects.filter(user = request.user, due_date__range=[timezone.now().date(), timezone.now().date() + timedelta(days = 7)], status=False).order_by('due_date')
			taskswpr = Task.objects.filter(user = request.user, project=None, status = False).order_by('due_date')
			projects = Project.objects.filter(user = request.user).order_by('due_date')
			form = TaskStatusForm()
			content = {
				'overdue_list': overdue,
				'tasks_list': week_tasks,
				'projects_list': projects,
				'form': form,
				'out_tasks': taskswpr,
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
			removetaskform = RemoveTaskForm()
			commentform = CommentForm()
			comments = Comment.objects.filter(task = task)
			context = {
				'removetaskform': removetaskform,
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

def remove_task(request):
	if request.user.is_authenticated():
		if request.method == 'POST':
			form = RemoveTaskForm(request.POST)
			if form.is_valid():
				task = Task.objects.get(pk = form.cleaned_data['task_id'])
				if request.user == task.user:
					task.delete()
				else:
					return HttpResponseRedirect("/login/")
				return HttpResponseRedirect("/tasks/")

