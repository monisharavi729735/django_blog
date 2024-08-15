from django.shortcuts import render

posts = [
    {
        'author':'auth1',
        'title' : 'title1',
        'content': 'post 1 content',
        'posted': '1st April 1989'
    },
    {
        'author':'auth2',
        'title' : 'title2',
        'content': 'post 2 content',
        'posted': '2nd April 1991'
    }
]

# Create your views here.
def home(request):
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})