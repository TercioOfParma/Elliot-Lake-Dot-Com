from django.shortcuts import render

# Create your views here.


def test(request):
    return render(request, "blog/test.html")


def projects(request):
    return render(request, "blog/projects.html")


def cv(request):
    return render(request, "blog/cv.html")


def bloghome(request):
    return render(request, "blog/bloghomepage.html")


def home(request):
    return render(request, "blog/home.html")

