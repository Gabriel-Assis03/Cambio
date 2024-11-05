from django.shortcuts import render
from .controller import coins_options


def exchange_page(request):
    data = coins_options()
    context = {
            'keys': data['keys'],
        }
    return render(request, 'exchange_page.html', context)
