from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.views.generic import TemplateView
from django.contrib.auth import views
from django.contrib.auth.models import User


from tasks.models import Task, Project, Comment

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



