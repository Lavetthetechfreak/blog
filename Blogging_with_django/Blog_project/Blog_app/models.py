from django.db import models

# Create your models here.

class Blog(models.Model):
	title = models.CharField(max_length=30)
	content = models.TextField()
	Timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
	Update = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __str__(self):

		return self.title

