from django.shortcuts import render

def index(rq):
    # function er modhhe j parameter pass kora hbe oita templte er age nam boshate hbe
    return render(rq,"index.html")