from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views import generic
from django.views.generic import TemplateView


from tasks.models import Task, User, Project, Comment
from tasks.forms import TaskForm

class IndexView(generic.ListView):
	template_name = 'tasks/index.html'
	context_object_name = 'tasks_list'

	def get_queryset(self):
		return Task.objects.all()

class DetailView(generic.DetailView):
	model = Task
	template_name = 'tasks/detail.html'


class MyFormView(generic.FormView):
	template_name = "tasks/create.html"
	form_class = TaskForm
	success_url = '/tasks/create/' #reverse_lazy('detail')


	def form_valid(self, form):
		form.save()
		return super().form_valid(form)


# def create(request):
# 	#task = Task.objects.create(title = title, description = description)
# 	#return render(request, 'tasks/detail.html', {'task': task})
# 	if request.method == 'POST':
# 		print('POST')
# 		form = TaskForm(request.POST)
# 		if form.is_valid():
# 			title = form.cleaned_data['title']
# 			description = form.cleaned_data['description']
# 			print('Yey')
# 			task = Task.objects.create(title = title, description = description)
# 			return HttpResponseRedirect('tasks/index')
# 	else:
# 		form = TaskForm()
# 	return render(request, 'tasks/create.html', {'form': form})
