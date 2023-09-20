from django.shortcuts import render

posts = [
    {
        'author': 'Saheed Bello',
        'title': 'Blog Post 1',
        'image': './IMG_1371.jpeg',
        'content': 'First post content',
        'date_posted': 'September 9, 2023'
    },
    {
        'author': 'Saheed Bello',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'September 10 2023'
    },
    {
        'author': 'Saheed Bello',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': 'September 15 2023'
    }
]
def home(request):
    context = {
        'posts': posts
    }

    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def base64_encode(data):
    if data:
        return base64.b64encode(data).decode('utf-8')
    else:
        return(None)