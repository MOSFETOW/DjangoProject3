

from django.shortcuts import render

def home(request):
    context = {
        "title": "Головна сторінка",
        "content": "Це головна сторінка сайту",
        "is_home": True
    }
    return render(request, "page.html", context)


def page1(request):
    context = {
        "title": "Сторінка 1",
        "content": "Це перша сторінка",
        "is_home": False
    }
    return render(request, "page.html", context)


def page2(request):
    context = {
        "title": "Сторінка 2",
        "content": "Це друга сторінка",
        "is_home": False
    }
    return render(request, "page.html", context)
