from django.shortcuts import render

posts = [
    {
        'author':'John Smith',
        'title' : 'Penguins',
        'content': 'I like penguins',
        'posted': '1st April 2023'
    },
    {
        'author':'Jane Doe',
        'title' : 'Turtles',
        'content': 'that\'s a cute turtle',
        'posted': '2nd April 2023'
    }
]

# Create your views here.
def home(request):
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})