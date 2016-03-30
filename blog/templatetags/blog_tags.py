from django.utils.safestring import mark_safe
import markdown
from django import template
from ..models import Post
from django.db.models import Count
# register a valid tag library
register = template.Library()



# A new template tag u can add a new name by addig name attribute like : @register .simple_tag(name='my_tag')
@register.simple_tag
# A fucnction return the total published posts
#
# Note u need to restart the Django server in order to use the new template tags and filter
def total_posts():
	return Post.published.count()
@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
	latest_posts = Post.published.order_by('-publish')[:count]
	return {'latest_posts': latest_posts}

@register.assignment_tag
def get_most_commented_posts(count=5):
	return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]

@register.filter(name='markdown')
def markdown_format(text):
	return mark_safe(markdown.markdown(text))