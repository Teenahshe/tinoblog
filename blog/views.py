from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blog
from django.views.generic.edit import FormMixin
from .forms import CommentForm
from django.views.generic.edit import ModelFormMixin
from django.http import HttpResponseForbidden
from django.urls import reverse

# Create your views here.
class HomeListView(ListView):
	template_name = 'index.html'
	queryset = Blog.objects.order_by('-date_published')
	paginate_by = 9

class BlogDetailView(DetailView):
	template_name = 'single-blog.html'
	queryset =Blog.objects.all()

