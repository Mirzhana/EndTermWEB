from rest_framework import generics
from .models import Post
from . import models
from . import serializers
from django.views import generic


class ListPosts(generic.ListView):
   ## queryset = models.Post.objects.all()
    ##serializer_class = serializers.PostSerializer

    model = Post
    paginate_by = 10



class DetailPosts(generic.DetailView):

    model = Post


