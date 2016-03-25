from django.db import models

# Create your models here.

class User(models.Model):
	email = models.CharField(max_length=200)
	password = models.CharField(max_length=200)

class Task(models.Model):
	"""docstring for task"""
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=1000)
	#comments = models.ForeignKey(Comment, on_delete=models.CASCADE)
	#status = Finished or Not
	#exp_time = models.DateTimeField('date published')

	def create(cls, title, description=None):
		task = cls(title=title, description=description)
		return task

class Project(models.Model):
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=1000)
	tasks = []  #list of tasks for that project # = models.ForeignKey(Question, on_delete=models.CASCADE)

class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	date = models.DateTimeField(auto_now_add=True, blank=True)
	title = models.CharField(max_length=200)
	text = models.CharField(max_length=1000)