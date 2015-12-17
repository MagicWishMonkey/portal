from .view import *


def get(request):
    return View(request).redirect("login", logout=True)
