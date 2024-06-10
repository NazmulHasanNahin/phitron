from django.shortcuts import *

# Create your views here.


def home(request):
    test = {"listjoint": ["python", "is", "best"],
            "value": 123,
            "date": "2024-06-10",
            "string": "hello world",
            "list": [5, 9, 13, 20],
            "filesize": 123456789,
            "cut": "Python is Fun",
            "foods": [
        {"name": "Apple", "category": "Fruit"},
        {"name": "Carrot", "category": "Vegetable"},
        {"name": "Banana", "category": "Fruit"},
        {"name": "Spinach", "category": "Vegetable"}],
        "greeting": "Hello, WORLD!",
        "titlecard": "hello world, this is django!",
        "quotes": ["Life is beautiful", "Enjoy the life", "Go for dream"],
        "items": ["Apple", "Banana", "Cherry", "Date", "Elderberry"],
        "long_text": "This is a very long text that needs to be truncated for display purposes."


    }
    return render(request, "index.html", test)
    # return HttpResponse("HIIII")
