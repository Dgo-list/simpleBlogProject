from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager

class PublishedManager(models.Manager):
	"""docstring for PublishedManager"""
	def get_queryset(self):
		return super(PublishedManager, self).get_queryset().filter(status='published')
		
class Post(models.Model):
	STATUS_CHOICES = (
		('draft', 'Draft'),
		('published', 'Published'),
	)
	title = models.CharField(max_length=250)
	slug = models.SlugField(max_length=250, unique_for_date='publish')
	author = models.ForeignKey(User, related_name='blog_posts')
	body = models.TextField()
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
	object = models.Manager()
	published = PublishedManager()
	tags = TaggableManager()
	class Meta:
		ordering = ('-publish',)

	def __str__ (self):
		return self.title

	# ...
	def get_absolute_url(self):
		return reverse('blog:post_detail',
						args=[self.publish.year, 
						self.publish.strftime('%m'), 
						self.publish.strftime('%d'), 
						self.slug])
# Class comments
class Comment(models.Model):
	post = models.ForeignKey(Post, related_name='comments')
	name = models.CharField(max_length=80)
	email = models.EmailField()
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updateed = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)
	class Meta:
		"""docstring for Meta"""
		ordering = ('created',)
	# returning action from the class
	def __str__(self):	
		return 'Comment by {} on {}'.format(self.name, self.post)