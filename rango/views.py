from django.shortcuts import render, HttpResponse


def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)
    # return HttpResponse("Rango says hey there partner!" + "<a href='/rango/about'>about</a>")


def about(request):
    context_dict = {'name': 'root'}
    return render(request, 'rango/about.html', context=context_dict)
    # return HttpResponse("Rango says here is the about page." + "<a href='/rango/'>index</a>")
