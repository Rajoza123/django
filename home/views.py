from django.shortcuts import render
from django.shortcuts import HttpResponse


def home(request):

    peoples = [
        {"name": "raj", "age": 21},
        {"name": "smit", "age": 23},
        {"name": "dilip", "age": 34},
    ]
    return render(request,"index.html",context={"peoples": peoples})


def success_page(request):
    return HttpResponse("<h1>This is a success page</h1>")
