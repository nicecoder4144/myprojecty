from django import template 
from django.db.models import Count
from ..models import Post


register = template.Library()


@register.inclusion_tag('tags/lastest_posts.html')#eng so'ngi postlar
def show_lastest_posts(count=5):
	lastest_posts = Post.objects.filter(status='active').order_by('-created_at')[:count]
	return {'lastest_posts':lastest_posts}



@register.inclusion_tag('tags/most_view.html')#eng so'ngi postlar
def most_view_posts():
	most_view = Post.objects.filter(status='active').order_by('-see')[:5]
	return {'most_view':most_view}