from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.views.generic import TemplateView


from tasks.models import Task, User, Project, Comment
from tasks.forms import TaskForm

class IndexView(TemplateView):
	template_name = 'index.html'