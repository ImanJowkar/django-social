from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
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


class PostDeleteView(View):
    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)
        if request.user.id == post.publisher.id:
            post.delete()
            messages.success(request, 'Post successfully deleted', 'success')
            return redirect('account:user-profile', request.user.id)
        messages.success(request, 'you dont have permission to delete this post.', 'danger')
        return redirect('account:user-profile', request.user.id)


class PostUpdateView(LoginRequiredMixin, View):
    def get(self, request):
        pass
