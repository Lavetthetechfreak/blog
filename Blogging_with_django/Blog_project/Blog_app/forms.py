from django import forms
from .models import Blog


#create my form here

class BlogForm(forms.ModelForm):
	
	class Meta:
		model = Blog
		fields = [
		   'title',
		   'content'
		]