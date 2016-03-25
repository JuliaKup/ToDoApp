from django import forms

class TaskForm(forms.Form):
    title = forms.CharField(label='title', max_length=200)
    description = forms.CharField(label='description', max_length=1000)