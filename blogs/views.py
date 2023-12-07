from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Blog


def blog_index(request):
    queryset = Blog.objects.values('id', 'title', 'author_id', 'created_at').filter(status='P', ).order_by(
        '-created_at')[:28]
    return render(
        request,
        'blogs/blog_index.html',
        {"blogs": queryset}
    )


def blog_info(request, blog_id: int):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(
        request,
        'blogs/blog_detail.html',
        {"blog": blog}
    )
