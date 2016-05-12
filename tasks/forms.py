from django import forms
import datetime
from django.forms.extras.widgets import SelectDateWidget
from django.forms.widgets import DateTimeInput
from tasks.models import Task, Comment

class TaskForm(forms.ModelForm):
	due_date = forms.DateTimeField(required=False, widget=SelectDateWidget)
	class Meta:
		model = Task
		fields = ['title', 'description', 'due_date']

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['title', 'text']

class TaskStatusForm(forms.Form):
	task_id = forms.IntegerField(required=True)