from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Post


def post_list(request):
    post_list = Post.objects.all()
    return render(request, 'blog/post_list.html', {
        'post_list': post_list,
    })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {
        'post': post,
    })


@login_required
# @require_POST
def post_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.like_users.add(request.user)
    post.like_count = post.like_users.count()
    post.save()
    return JsonResponse({'ok': True, 'like_count': post.like_count}, safe=False)
