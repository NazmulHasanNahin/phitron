from django.shortcuts import render

# Create your views here.


def home(request):
    d={"author" : "rahim" , "age" : 29 ,"list":["python","is","best"],"courses":[
        {
            "id":1,
            "name" : "python",
            "fee" : 6500,
        },
        {
            "id":2,
            "name" : "django",
            "fee" : 5500,
        },
        {
            "id":3,
            "name" : "c",
            "fee" : 4500,
        }
    ]}
    return render(request,"home.html",d)