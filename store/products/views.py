from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'tittle': 'Mangastore',
        'username': 'Sanzhar',
    }
    return render(request, 'products/index.html', context)

def about(request):
    return render(request, 'products/about.html')
def news(request):
    return render(request, 'products/news.html')

def products(request):
    context = {
        'title': 'Mangastore - products',
        'products': [
            {
                'image': '/static/img/aot1.jpg',
                'name': 'Attack on Titan Vol. 1',
                'price': 2000,
                'description': 'In this post-apocalyptic sci-fi story, humanity has been devastated by the bizarre, giant humanoids known as the Titans',
            },
            {
                'image': '/static/img/spy9.jpg',
                'name': 'Spy x Family, Vol. 9',
                'price': 1800,
                'description': 'An action-packed comedy about a fake family that includes a spy, an assassin and a telepath!',
            },
            {
                'image': '/static/img/vinlandsaga1.jpeg',
                'name': 'Vinland Saga 1',
                'price': 2500,
                'description': 'Vinland saga  is a Japanese historical manga series written and illustrated by Makoto Yukimura.',
            },

        ]

    }
    return render(request, 'products/products.html', context)