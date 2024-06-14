from django.shortcuts import render
from .forms import contactform
from .forms import contactform, StudentData ,passwordValidation
# Create your views here.


def index(rq):
    d = [{
        "userId": 1,
        "id": 1,
        "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
        "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
    },
        {
            "userId": 1,
            "id": 2,
            "title": "qui est esse",
            "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
    },
        {
            "userId": 1,
            "id": 3,
            "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
            "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut"
    },
        {
            "userId": 1,
            "id": 4,
            "title": "eum et est occaecati",
            "body": "ullam et saepe reiciendis voluptatem adipisci\nsit amet autem assumenda provident rerum culpa\nquis hic commodi nesciunt rem tenetur doloremque ipsam iure\nquis sunt voluptatem rerum illo velit"
    },
        {
            "userId": 1,
            "id": 5,
            "title": "nesciunt quas odio",
            "body": "repudiandae veniam quaerat sunt sed\nalias aut fugiat sit autem sed est\nvoluptatem omnis possimus esse voluptatibus quis\nest aut tenetur dolor neque"
    }]
    return render(rq, "index.html",  {'d': d})


# new views

def about(rq):
    name = None
    email = None
    select = None
    if rq.method == "POST":
        name = rq.POST.get("username")
        email = rq.POST.get("useremail")
        select = rq.POST.get("select")
        return render(rq, "about.html", {"name": name, "email": email, "select": select})
    else:
        return render(rq, "about.html")


def form_submit(rq):
    return render(rq, "form.html")


def DjangoForm(rq):
    if rq.method == "POST":
        form = contactform(rq.POST, rq.FILES)
        if form.is_valid():
            # file = form.cleaned_data["file"]
            # with open("./firstapp/upload/" + file.name ,"wb+") as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
    else:
        form = contactform()
    return render(rq, "django_form.html", {"form": form})


def StudentForm(rq):
    if rq.method == "POST":
        form = StudentData(rq.POST, rq.FILES)
        if form.is_valid():
            # file = form.cleaned_data["file"]
            # with open("./firstapp/upload/" + file.name ,"wb+") as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
    else:
        form = StudentData()
    return render(rq, "django_form.html", {"form": form})


def passwordValidationProject(rq):
    if rq.method == "POST":
        form = passwordValidation(rq.POST, rq.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = passwordValidation()
    return render(rq, "django_form.html", {"form": form})
