from django.shortcuts import render


def exchange_page(request):
    context = {}
    return render(request, 'exchange_page.html', context)