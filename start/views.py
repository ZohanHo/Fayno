from django.shortcuts import render


def start(request):
    return render(request, 'start_page/start_page.html')