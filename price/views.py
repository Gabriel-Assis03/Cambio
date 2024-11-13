from django.shortcuts import render
from .controller import coins_options, caculate_value


def exchange_page(request):
    data = coins_options()
    if request.method == "POST":
        finalValue = caculate_value(
            request.POST['quant-value'],
            request.POST['coin-now'],
            request.POST['coin-new']
            )
    context = {
            'keys': data['keys'],
            'finalValue': finalValue
        }
    return render(request, 'exchange_page.html', context)
