from django.shortcuts import render

def permission_denied(request):
    return render(request, "403.html")


def page_not_found(request):
    return render(request, "404.html")


def page_error(request):
    return render(request, "500.html")