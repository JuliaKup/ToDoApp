from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
	"""docstring for task"""
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=1000)
	status = models.BooleanField(default=False)
	due_date = models.DateTimeField(blank=True, default=None, null=True)
	#project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)

	def __str__(self):
		return self.title

class Project(models.Model):
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=1000)
	tasks = []  #list of tasks for that project # = models.ForeignKey(Question, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	task = models.ForeignKey(Task, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True, blank=False)
	title = models.CharField(max_length=200)
	text = models.CharField(max_length=1000)

	def __str__(self):
		return self.title