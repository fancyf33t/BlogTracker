from django.shortcuts import render

# Create your views here.
def index(request):
    """The home page for blog tracker"""
    return render(request, 'blog_tracker_dir/index.html')