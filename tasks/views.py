from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Task
from django.http import Http404
from .forms import TaskForm

def index(request):
	tasks_list = Task.objects.all()
	template = loader.get_template('tasks/index.html')
	context = {
		'tasks_list': tasks_list,
	}
	return HttpResponse(template.render(context, request))

def create_task(request):
	if request.method == 'POST':
		form = TaskForm(request.POST)
		return HttpResponseRedirect('/')
	else:
		form = TaskForm()
	return HttpResponseRedirect('/')

def detail(request, task_id):
	t = get_object_or_404(Task, pk = task_id)
	return render(request, 'tasks/detail.html', {'task': t})
