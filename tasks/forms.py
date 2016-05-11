from django import forms
from tasks.models import Task, Comment
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['title', 'description']

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['title', 'text']