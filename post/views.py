from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404
from post.models import Post


# Create your views here.

class PostView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'post/all-post.html', {'posts': posts})


class PostDetailView(View):
    def get(self, request, post_id, post_slug):
        post = get_object_or_404(Post, pk=post_id, slug=post_slug)
        return render(request, 'post/post-detail.html', {'post': post})
