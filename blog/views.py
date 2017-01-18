from django.shortcuts import render
from django.views import generic

from .models import Author, Blog, Comment


# Create your views here.
def index(request):
    """
    View function for home page site
    It has numbers of various models
    """
    # Number of authors
    num_author = Author.objects.count()  # all() is implied
    num_blog = Blog.objects.count()
    num_comment = Comment.objects.count()
    average_comment = num_comment / num_blog

    return render(
        request,
        'blog/index.html',
        {'num_author': num_author,
            'num_blog': num_blog,
            'num_comment': num_comment,
            'average_comment': average_comment}
    )


class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 3


class BlogDetailView(generic.DetailView):
    model = Blog


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 3


class AuthorDetailView(generic.DetailView):
    model = Author
