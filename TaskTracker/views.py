from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.views.generic import TemplateView
from django.contrib.auth import views
from django.contrib.auth.models import User
from django.utils import timezone

from tasks.models import Task, Project, Comment
from tasks.forms import TaskForm, ProjectForm

def index(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect("/tasks/")
	else:
		return render(request, "index.html")

def login(request):
	template_response = views.login(request, template_name='registration/login.html',
						redirect_field_name='next', authentication_form=AuthenticationForm,
						current_app=None, extra_context=None)
	return template_response

def logout(request):
	template_response = views.logout(request, next_page='tasks/')
	return template_response


class RegisterView(generic.FormView):
	template_name = "registration/register.html"
	model = User
	success_url = "/tasks/"


	def form_valid(self, form):
		form.save()
		return super().form_valid(form)

def create_project(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			form = ProjectForm(request.POST)
			if form.is_valid():
				project = form.save(commit=False)
				project.user = request.user
				project.creation_date = timezone.now()
				project.save()
				return HttpResponseRedirect("/tasks/")
		else:
			form = ProjectForm
		return render(request, 'create_project.html', {'form': form})
	else:
		return HttpResponseRedirect("/login/")

def project(request, pk):
	try:
		project = Project.objects.get(pk=pk)
	except Project.DoesNotExist:
		return HttpResponseRedirect("/tasks/")
	if request.user == project.user:
		if request.method == "POST":
			form = TaskForm(request.POST)
			if form.is_valid():
				task = form.save(commit=False)
				task.user = request.user
				task.project = project
				task.creation_date = timezone.now()
				task.save()
				return HttpResponseRedirect("/tasks/")
		else:
			tasks = Task.objects.filter(project = project).order_by('due_date')
			form = TaskForm()
			context = {
				'form': form,
				'project': project,
				'tasks_list': tasks,
			}
			return render(request, 'project.html', context)
	else:
		return HttpResponseRedirect("/login/")

