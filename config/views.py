from django.shortcuts import render


def main_home(request):
    return render(request, 'core/base.html')