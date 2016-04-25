from django import forms
from tasks.models import Task

class TaskForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['title', 'description']
    #title = forms.CharField(label='c', max_length=200)
    #description = forms.CharField(label='description', max_length=1000)