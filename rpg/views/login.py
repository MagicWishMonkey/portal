from .view import *


def get(request):
    return View(request).render("login.html")


@csrf_exempt
def post(request):
    username = request.POST.get("username", None)
    password = request.POST.get("password", None)
    return View(request).render("login.html")
