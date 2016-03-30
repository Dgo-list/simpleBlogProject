from django import forms
from .models import Comment

class EmailPostform(forms.Form):
	"""docstring for EmailPostform"""
	# Each field type has a default widget that determines how the field is displayed in HTML.
	#
	# The default widget can be overridden with the widget attribute
	name = forms.CharField(max_length=25)  # <input type="text">
	email = forms.EmailField() # <input type="email">
	to = forms.EmailField() # <input type="email">
	comments = forms.CharField(required=False, widget=forms.Textarea) # widget attribute changing the input type to Textarea

# adding the Comment form from Comment Model
class CommentForm(forms.ModelForm):
	# 
	class Meta:
		model = Comment
		fields = ('name', 'email', 'body')
